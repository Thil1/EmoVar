"""
情境编码器模块
将文本情境描述编码为固定维度的向量表示
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Union, List


class SituationEncoder:
    """
    使用 sentence-transformers 将文本编码为向量
    
    参数:
        model_name: 模型名称或路径，默认 'all-MiniLM-L6-v2'
                   可传入其他模型如 'all-mpnet-base-v2' 或本地路径
        device: 运行设备，默认 'cpu'，可选 'cuda'
    """
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2', device: str = 'cpu'):
        self.model = SentenceTransformer(model_name, device=device)
        self.model_name = model_name
        self.device = device
    
    def encode(self, text: Union[str, List[str]]) -> np.ndarray:
        """
        将文本编码为向量
        
        参数:
            text: 输入文本（字符串或字符串列表）
        
        返回:
            numpy数组
            - 单个文本: shape (dim,)
            - 多个文本: shape (n, dim)
        """
        embedding = self.model.encode(text, normalize_embeddings=False)
        return embedding
    
    @property
    def embedding_dim(self) -> int:
        """返回模型输出的向量维度"""
        return self.model.get_sentence_embedding_dimension()
    
    def __repr__(self):
        return f"SituationEncoder(model='{self.model_name}', dim={self.embedding_dim}, device='{self.device}')"


if __name__ == '__main__':
    import sys
    
    encoder = SituationEncoder()
    print(f"已加载编码器: {encoder}")
    print(f"向量维度: {encoder.embedding_dim}")
    
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("请输入情境描述: ")
    
    vector = encoder.encode(text)
    print(f"\n输入文本: {text}")
    print(f"向量维度: {vector.shape}")
    print(f"向量前10个值: {vector[:10]}")
    print(f"向量范数: {np.linalg.norm(vector):.4f}")
