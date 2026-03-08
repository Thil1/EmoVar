"""
模型注入模块
将情感状态注入生成模型，产生情感化语言输出
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Optional, List, Union
import numpy as np


class ModelInjector:
    """
    模型注入类
    
    将情感向量通过 prompt 拼接方式注入生成模型，
    控制生成文本的情感风格。
    
    参数:
        model_name: 生成模型名称或路径，默认 'gpt2'
        device: 运行设备，默认 'cuda'
        max_length: 最大生成长度
        temperature: 生成温度
        top_p: nucleus sampling 参数
        top_k: top-k sampling 参数
    """
    
    def __init__(
        self,
        model_name: str = 'gpt2',
        device: str = 'cuda',
        max_length: int = 100,
        temperature: float = 0.8,
        top_p: float = 0.9,
        top_k: int = 50
    ):
        self.model_name = model_name
        self.device = device if torch.cuda.is_available() else 'cpu'
        self.max_length = max_length
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
    
    def _vector_to_description(self, state_vector: np.ndarray) -> str:
        """
        将情感向量转换为自然语言描述
        
        这是一个简化版本，实际应用中可以使用更复杂的映射
        """
        mean_val = np.mean(state_vector)
        std_val = np.std(state_vector)
        max_val = np.max(state_vector)
        min_val = np.min(state_vector)
        
        intensity = (max_val - min_val) / (std_val + 1e-6)
        
        descriptions = []
        
        if intensity > 1.5:
            descriptions.append("情感强烈")
        elif intensity > 0.8:
            descriptions.append("情感适中")
        else:
            descriptions.append("情感平和")
        
        if mean_val > 0.1:
            descriptions.append("偏向积极")
        elif mean_val < -0.1:
            descriptions.append("偏向内敛")
        else:
            descriptions.append("中性表达")
        
        if std_val > 0.3:
            descriptions.append("情绪多变")
        else:
            descriptions.append("情绪稳定")
        
        return "，".join(descriptions)
    
    def inject(
        self,
        state_vector: np.ndarray,
        base_prompt: str = ""
    ) -> str:
        """
        将情感向量转换为 prompt 修饰
        
        参数:
            state_vector: 情感状态向量
            base_prompt: 基础 prompt
        
        返回:
            注入情感信息后的完整 prompt
        """
        description = self._vector_to_description(state_vector)
        
        injected_prompt = f"[情感状态: {description}]\n{base_prompt}"
        
        return injected_prompt
    
    def generate(
        self,
        prompt: str,
        state_vector: Optional[np.ndarray] = None,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None
    ) -> str:
        """
        生成情感化文本
        
        参数:
            prompt: 输入 prompt
            state_vector: 情感状态向量（可选）
            max_new_tokens: 最大新token数
            temperature: 生成温度
            top_p: nucleus sampling 参数
            top_k: top-k sampling 参数
        
        返回:
            生成的文本
        """
        if state_vector is not None:
            full_prompt = self.inject(state_vector, prompt)
        else:
            full_prompt = prompt
        
        inputs = self.tokenizer(full_prompt, return_tensors='pt', padding=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        gen_max_new = max_new_tokens if max_new_tokens is not None else self.max_length
        gen_temp = temperature if temperature is not None else self.temperature
        gen_top_p = top_p if top_p is not None else self.top_p
        gen_top_k = top_k if top_k is not None else self.top_k
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=gen_max_new,
                temperature=gen_temp,
                top_p=gen_top_p,
                top_k=gen_top_k,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        if state_vector is not None:
            injected_prompt = self.inject(state_vector, prompt)
            if generated_text.startswith(injected_prompt):
                generated_text = generated_text[len(injected_prompt):].strip()
        
        return generated_text
    
    def __repr__(self):
        return f"ModelInjector(model='{self.model_name}', device='{self.device}')"


if __name__ == '__main__':
    from situation_encoder import SituationEncoder
    from infinite_state import InfiniteState
    
    print("初始化编码器和状态管理...")
    encoder = SituationEncoder()
    state = InfiniteState(dim=encoder.embedding_dim)
    
    print("\n初始化生成模型（可能需要下载）...")
    injector = ModelInjector(device='cpu')
    print(f"生成器: {injector}")
    
    test_situations = [
        "阳光明媚的春天早晨，鸟儿在歌唱",
        "寂静的夜晚，独自望着星空"
    ]
    
    for i, situation in enumerate(test_situations, 1):
        print(f"\n{'='*50}")
        print(f"情境 {i}: {situation}")
        
        vec = encoder.encode(situation)
        state.update(vec, source=situation)
        
        prompt = "今天的心情"
        generated = injector.generate(prompt, state.vector)
        
        print(f"生成结果: {generated}")
