"""
EmoVar 全局配置管理
管理模型路径、向量维度、超参数等配置
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """全局配置类"""
    
    # 情境编码器配置
    encoder_model: str = 'all-MiniLM-L6-v2'
    encoder_device: str = 'cpu'
    
    # 生成模型配置
    generator_model: str = 'gpt2'
    generator_device: str = 'cuda'
    
    # 状态管理配置
    state_fusion_alpha: float = 0.7  # 新状态权重（融合时）
    state_decay_rate: float = 0.95   # 状态衰减率
    
    # 生成参数配置
    max_length: int = 100
    temperature: float = 0.8
    top_p: float = 0.9
    top_k: int = 50
    
    # 数据配置
    data_dir: str = './data'
    
    @classmethod
    def from_env(cls):
        """从环境变量加载配置"""
        return cls(
            encoder_model=os.getenv('EMOVAR_ENCODER_MODEL', 'all-MiniLM-L6-v2'),
            encoder_device=os.getenv('EMOVAR_ENCODER_DEVICE', 'cpu'),
            generator_model=os.getenv('EMOVAR_GENERATOR_MODEL', 'gpt2'),
            generator_device=os.getenv('EMOVAR_GENERATOR_DEVICE', 'cuda'),
            state_fusion_alpha=float(os.getenv('EMOVAR_FUSION_ALPHA', '0.7')),
            state_decay_rate=float(os.getenv('EMOVAR_DECAY_RATE', '0.95')),
            max_length=int(os.getenv('EMOVAR_MAX_LENGTH', '100')),
            temperature=float(os.getenv('EMOVAR_TEMPERATURE', '0.8')),
            top_p=float(os.getenv('EMOVAR_TOP_P', '0.9')),
            top_k=int(os.getenv('EMOVAR_TOP_K', '50')),
            data_dir=os.getenv('EMOVAR_DATA_DIR', './data'),
        )


# 默认配置实例
default_config = Config()
