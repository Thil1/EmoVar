"""
无限状态管理模块
管理智能体的连续情感状态向量
"""

import numpy as np
from typing import Optional, List, Tuple
from dataclasses import dataclass, field


@dataclass
class StateRecord:
    """状态记录，用于存储历史状态"""
    vector: np.ndarray
    timestamp: float
    source: str = "unknown"


class InfiniteState:
    """
    无限状态管理类
    
    用纯连续向量表示智能体的内部情感状态，
    支持状态更新（加权融合）、衰减和重置。
    
    参数:
        dim: 向量维度，默认 384（与 all-MiniLM-L6-v2 一致）
        fusion_alpha: 新状态权重，范围 [0, 1]，默认 0.7
        decay_rate: 状态衰减率，范围 [0, 1]，默认 0.95
        keep_history: 是否保存历史状态，默认 True
    """
    
    def __init__(
        self,
        dim: int = 384,
        fusion_alpha: float = 0.7,
        decay_rate: float = 0.95,
        keep_history: bool = True
    ):
        self.dim = dim
        self.fusion_alpha = fusion_alpha
        self.decay_rate = decay_rate
        self.keep_history = keep_history
        
        self._vector: Optional[np.ndarray] = None
        self._history: List[StateRecord] = []
        self._update_count: int = 0
    
    @property
    def vector(self) -> Optional[np.ndarray]:
        """当前状态向量"""
        return self._vector
    
    @property
    def is_initialized(self) -> bool:
        """状态是否已初始化"""
        return self._vector is not None
    
    def update(
        self,
        situation_vector: np.ndarray,
        source: str = "situation",
        weight: Optional[float] = None
    ) -> np.ndarray:
        """
        根据情境向量更新状态（加权融合）
        
        新状态 = fusion_alpha * 情境向量 + (1 - fusion_alpha) * 旧状态
        
        参数:
            situation_vector: 情境编码向量
            source: 状态来源标识
            weight: 自定义融合权重，None则使用fusion_alpha
        
        返回:
            更新后的状态向量
        """
        situation_vector = np.asarray(situation_vector)
        
        if situation_vector.ndim != 1:
            raise ValueError(f"期望1维向量，得到 {situation_vector.ndim} 维")
        
        if len(situation_vector) != self.dim:
            raise ValueError(f"向量维度不匹配: 期望 {self.dim}, 得到 {len(situation_vector)}")
        
        alpha = weight if weight is not None else self.fusion_alpha
        
        if not self.is_initialized:
            self._vector = situation_vector.copy()
        else:
            self._vector = alpha * situation_vector + (1 - alpha) * self._vector
        
        self._update_count += 1
        
        if self.keep_history:
            import time
            record = StateRecord(
                vector=self._vector.copy(),
                timestamp=time.time(),
                source=source
            )
            self._history.append(record)
        
        return self._vector.copy()
    
    def decay(self, rate: Optional[float] = None) -> np.ndarray:
        """
        状态衰减（模拟情感消退）
        
        新状态 = decay_rate * 当前状态
        
        参数:
            rate: 自定义衰减率，None则使用decay_rate
        
        返回:
            衰减后的状态向量
        """
        if not self.is_initialized:
            raise RuntimeError("状态未初始化，无法衰减")
        
        decay_r = rate if rate is not None else self.decay_rate
        self._vector = decay_r * self._vector
        return self._vector.copy()
    
    def reset(self) -> None:
        """重置状态"""
        self._vector = None
        self._history.clear()
        self._update_count = 0
    
    def get_history(self, last_n: int = 10) -> List[StateRecord]:
        """获取最近N条历史记录"""
        return self._history[-last_n:] if self._history else []
    
    def get_similarity_to(self, other_vector: np.ndarray) -> float:
        """计算当前状态与目标向量的余弦相似度"""
        if not self.is_initialized:
            raise RuntimeError("状态未初始化")
        
        other_vector = np.asarray(other_vector)
        dot = np.dot(self._vector, other_vector)
        norm1 = np.linalg.norm(self._vector)
        norm2 = np.linalg.norm(other_vector)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot / (norm1 * norm2)
    
    def __repr__(self):
        status = "已初始化" if self.is_initialized else "未初始化"
        return f"InfiniteState(dim={self.dim}, status={status}, updates={self._update_count})"


if __name__ == '__main__':
    from situation_encoder import SituationEncoder
    
    encoder = SituationEncoder()
    state = InfiniteState(dim=encoder.embedding_dim)
    
    print(f"初始状态: {state}")
    
    text1 = "今天天气晴朗，阳光明媚"
    vec1 = encoder.encode(text1)
    state.update(vec1, source=text1)
    print(f"\n情境1: {text1}")
    print(f"状态向量前5维: {state.vector[:5]}")
    
    text2 = "突然下起了大雨，道路泥泞"
    vec2 = encoder.encode(text2)
    state.update(vec2, source=text2)
    print(f"\n情境2: {text2}")
    print(f"状态向量前5维: {state.vector[:5]}")
    
    print(f"\n与情境1的相似度: {state.get_similarity_to(vec1):.4f}")
    print(f"与情境2的相似度: {state.get_similarity_to(vec2):.4f}")
    
    state.decay()
    print(f"\n衰减后向量前5维: {state.vector[:5]}")
