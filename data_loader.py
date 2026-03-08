"""
数据加载模块
加载情境数据集（TXT格式）
"""

import os
from typing import List, Iterator, Optional
from pathlib import Path


class DataLoader:
    """
    数据加载类
    
    支持从 TXT 文件加载情境数据（每行一个情境）
    
    参数:
        filepath: 数据文件路径
        encoding: 文件编码，默认 'utf-8'
    """
    
    def __init__(self, filepath: str, encoding: str = 'utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self._data: Optional[List[str]] = None
    
    def load(self) -> List[str]:
        """
        加载所有数据
        
        返回:
            情境文本列表
        """
        if self._data is not None:
            return self._data
        
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"文件不存在: {self.filepath}")
        
        with open(self.filepath, 'r', encoding=self.encoding) as f:
            lines = f.readlines()
        
        self._data = [line.strip() for line in lines if line.strip()]
        return self._data
    
    def batch_iter(self, batch_size: int = 1) -> Iterator[List[str]]:
        """
        批量迭代数据
        
        参数:
            batch_size: 批大小
        
        Yields:
            批量情境文本列表
        """
        data = self.load()
        
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]
    
    def __len__(self) -> int:
        """返回数据数量"""
        return len(self.load())
    
    def __iter__(self) -> Iterator[str]:
        """迭代所有数据"""
        return iter(self.load())
    
    def __repr__(self):
        count = len(self._data) if self._data else "未加载"
        return f"DataLoader(filepath='{self.filepath}', count={count})"


def create_sample_data(filepath: str = './data/situations.txt') -> str:
    """
    创建示例数据文件
    
    参数:
        filepath: 目标文件路径
    
    返回:
        创建的文件路径
    """
    sample_situations = [
        "清晨的阳光透过窗户洒进房间，温暖而柔和",
        "暴风雨中的街道，行人匆匆躲避",
        "安静的图书馆里，只有翻书的声音",
        "热闹的集市，叫卖声此起彼伏",
        "深夜的办公室，只有电脑屏幕的光",
        "公园里孩子们欢快地奔跑玩耍",
        "山顶俯瞰云海，心胸开阔",
        "旧照片唤起了美好的回忆",
        "等待重要消息的焦虑时刻",
        "完成挑战后的成就感"
    ]
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sample_situations))
    
    return filepath


if __name__ == '__main__':
    sample_path = create_sample_data()
    print(f"已创建示例数据: {sample_path}")
    
    loader = DataLoader(sample_path)
    print(f"\n数据加载器: {loader}")
    
    print(f"\n总数据量: {len(loader)}")
    
    print("\n所有情境:")
    for i, situation in enumerate(loader, 1):
        print(f"  {i}. {situation}")
    
    print("\n批量迭代 (batch_size=3):")
    for batch_idx, batch in enumerate(loader.batch_iter(batch_size=3), 1):
        print(f"  Batch {batch_idx}: {batch}")
