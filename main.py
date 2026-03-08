"""
EmoVar 主程序入口
整合所有模块，实现情境驱动的情感化语言生成
"""

import sys
import argparse
from typing import Optional

from config import Config, default_config
from situation_encoder import SituationEncoder
from infinite_state import InfiniteState
from model_injector import ModelInjector
from data_loader import DataLoader, create_sample_data


class EmoVarPipeline:
    """
    EmoVar 完整流程管道
    
    整合编码器、状态管理、生成模型，
    实现从情境到情感化文本的完整流程。
    
    参数:
        config: 配置对象，默认使用 default_config
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or default_config
        
        print("初始化 EmoVar 管道...")
        
        print(f"  [1/3] 加载情境编码器: {self.config.encoder_model}")
        self.encoder = SituationEncoder(
            model_name=self.config.encoder_model,
            device=self.config.encoder_device
        )
        
        print(f"  [2/3] 初始化状态管理: dim={self.encoder.embedding_dim}")
        self.state = InfiniteState(
            dim=self.encoder.embedding_dim,
            fusion_alpha=self.config.state_fusion_alpha,
            decay_rate=self.config.state_decay_rate
        )
        
        print(f"  [3/3] 加载生成模型: {self.config.generator_model}")
        self.generator = ModelInjector(
            model_name=self.config.generator_model,
            device=self.config.generator_device,
            max_length=self.config.max_length,
            temperature=self.config.temperature,
            top_p=self.config.top_p,
            top_k=self.config.top_k
        )
        
        print("EmoVar 管道初始化完成！\n")
    
    def process(
        self,
        situation: str,
        prompt: str = "",
        update_state: bool = True
    ) -> dict:
        """
        处理单个情境
        
        参数:
            situation: 情境描述文本
            prompt: 生成提示文本
            update_state: 是否更新状态
        
        返回:
            包含向量、生成结果等信息的字典
        """
        situation_vec = self.encoder.encode(situation)
        
        if update_state:
            self.state.update(situation_vec, source=situation)
        
        current_state_vec = self.state.vector
        
        generated_text = self.generator.generate(prompt, current_state_vec)
        
        return {
            'situation': situation,
            'situation_vector': situation_vec,
            'state_vector': current_state_vec,
            'prompt': prompt,
            'generated_text': generated_text,
            'state_info': str(self.state)
        }
    
    def process_batch(
        self,
        situations: list,
        prompt: str = "",
        reset_between: bool = False
    ) -> list:
        """
        批量处理情境
        
        参数:
            situations: 情境文本列表
            prompt: 生成提示文本
            reset_between: 每个情境之间是否重置状态
        
        返回:
            结果字典列表
        """
        results = []
        
        for i, situation in enumerate(situations, 1):
            if reset_between:
                self.state.reset()
            
            result = self.process(situation, prompt, update_state=True)
            results.append(result)
            
            print(f"\n[{i}/{len(situations)}] 情境: {situation}")
            print(f"生成: {result['generated_text']}")
        
        return results
    
    def reset_state(self):
        """重置状态"""
        self.state.reset()
    
    def decay_state(self):
        """状态衰减"""
        if self.state.is_initialized:
            self.state.decay()


def interactive_mode(pipeline: EmoVarPipeline):
    """交互模式"""
    print("\n" + "="*60)
    print("EmoVar 交互模式")
    print("="*60)
    print("输入情境描述，系统将生成情感化文本")
    print("命令:")
    print("  /reset  - 重置状态")
    print("  /decay  - 状态衰减")
    print("  /state  - 查看状态")
    print("  /quit   - 退出程序")
    print("="*60 + "\n")
    
    while True:
        try:
            user_input = input("输入情境 (或命令): ").strip()
            
            if not user_input:
                continue
            
            if user_input == '/quit':
                print("退出程序。")
                break
            
            elif user_input == '/reset':
                pipeline.reset_state()
                print("状态已重置。\n")
                continue
            
            elif user_input == '/decay':
                pipeline.decay_state()
                print("状态已衰减。\n")
                continue
            
            elif user_input == '/state':
                print(f"{pipeline.state}\n")
                continue
            
            prompt = input("输入生成提示 (留空则无提示): ").strip()
            
            result = pipeline.process(user_input, prompt if prompt else "")
            
            print(f"\n状态: {result['state_info']}")
            print(f"生成: {result['generated_text']}\n")
            
        except KeyboardInterrupt:
            print("\n\n程序被中断。")
            break
        except Exception as e:
            print(f"错误: {e}\n")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='EmoVar: 情境驱动的情感化语言生成系统'
    )
    
    parser.add_argument(
        '--encoder-model',
        default='all-MiniLM-L6-v2',
        help='情境编码器模型'
    )
    
    parser.add_argument(
        '--generator-model',
        default='gpt2',
        help='生成模型'
    )
    
    parser.add_argument(
        '--device',
        default='cpu',
        choices=['cpu', 'cuda'],
        help='运行设备'
    )
    
    parser.add_argument(
        '--input-file',
        help='输入文件路径（TXT格式）'
    )
    
    parser.add_argument(
        '--prompt',
        default='',
        help='生成提示文本'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='进入交互模式'
    )
    
    parser.add_argument(
        '--sample-data',
        action='store_true',
        help='使用示例数据'
    )
    
    args = parser.parse_args()
    
    config = Config(
        encoder_model=args.encoder_model,
        generator_model=args.generator_model,
        encoder_device=args.device,
        generator_device=args.device
    )
    
    pipeline = EmoVarPipeline(config)
    
    if args.interactive:
        interactive_mode(pipeline)
        return
    
    if args.sample_data:
        print("使用示例数据...")
        sample_path = create_sample_data()
        loader = DataLoader(sample_path)
        situations = loader.load()
        
        prompt = args.prompt if args.prompt else "此刻的感受"
        pipeline.process_batch(situations, prompt)
        return
    
    if args.input_file:
        print(f"从文件加载: {args.input_file}")
        loader = DataLoader(args.input_file)
        situations = loader.load()
        
        prompt = args.prompt if args.prompt else ""
        pipeline.process_batch(situations, prompt)
        return
    
    interactive_mode(pipeline)


if __name__ == '__main__':
    main()
