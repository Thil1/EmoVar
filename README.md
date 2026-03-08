# EmoVar - 情境驱动的情感化语言生成

## 🚀 快速开始（一条命令安装）

```bash
pip install -r requirements.txt && python main.py --interactive
```

---

## 📖 介绍

EmoVar 是一个创新的情感化语言生成系统。它不预设任何情感标签，而是用连续向量表示智能体的内部情感状态。输入情境描述，系统会自动编码、融合状态，并生成符合该情境的情感化语言。

**核心思想**：让用户从生成的文本中体会情感，而不是识别情感类别。

---

## 💻 一键安装

### 前置要求

- Python 3.8 或更高版本

### 安装命令

```bash
# Windows / Linux / macOS 通用
pip install -r requirements.txt
```

安装过程会自动下载：
- `sentence-transformers`（情境编码）
- `transformers`（文本生成）
- `torch`（深度学习框架）
- `numpy`（向量运算）

**预计下载量**：约600MB（首次运行时）
- `all-MiniLM-L6-v2`: ~90MB
- `gpt2`: ~500MB

---

## 🎯 三种使用方式

### 1. 交互模式（最简单）

```bash
python main.py --interactive
```

直接对话，输入情境即可：

```
输入情境: 今天阳光明媚，心情很好
输入提示: 此刻的感受
输出: 温暖的阳光洒在心间，一切都充满希望...
```

**交互命令**：
- `/reset` - 重置状态
- `/decay` - 情绪衰减
- `/state` - 查看当前状态
- `/quit` - 退出程序

---

### 2. 使用示例数据

```bash
python main.py --sample-data
```

自动创建10个示例情境并批量处理。

---

### 3. 文件批处理

```bash
python main.py --input-file ./situations.txt --prompt "我想说"
```

从TXT文件读取情境（每行一个）。

---

## 🛠️ 高级选项

### 指定模型

```bash
# 使用更大的编码器
python main.py --encoder-model all-mpnet-base-v2

# 使用 GPT-2 中等模型
python main.py --generator-model gpt2-medium

# 使用其他生成模型
python main.py --generator-model microsoft/DialoGPT-medium
```

### GPU 加速

```bash
python main.py --device cuda --interactive
```

需要 NVIDIA GPU 和 CUDA 支持。

---

## 📁 数据文件格式

创建 `situations.txt`（UTF-8编码）：

```
清晨的阳光透过窗户洒进房间
暴风雨中的街道，行人匆匆躲避
安静的图书馆里，只有翻书的声音
热闹的集市，叫卖声此起起彼伏
山顶俯瞰云海，心胸开阔
```

**每行一个情境，自动批量处理。**

---

## 🔧 模块独立测试

### 测试编码器

```bash
python situation_encoder.py
```

输出情境的384维向量表示。

### 测试状态管理

```bash
python infinite_state.py
```

演示状态融合和衰减效果。

### 测试生成模型

```bash
python model_injector.py
```

测试情感化文本生成。

---

## 📚 技术架构

```
输入情境文本
    ↓
┌─────────────────────┐
│ SituationEncoder    │  编码为384维向量
│ (all-MiniLM-L6-v2)  │
└─────────────────────┘
    ↓
┌─────────────────────┐
│ InfiniteState       │  加权融合状态
│ (连续情感向量)      │  update / decay / reset
└─────────────────────┘
    ↓
┌─────────────────────┐
│ ModelInjector       │  prompt拼接注入
│ (gpt2)              │  生成情感化文本
└─────────────────────┘
    ↓
输出情感化语言
```

---

## ⚙️ 配置说明

### config.py 关键参数

```python
# 编码器配置
encoder_model = 'all-MiniLM-L6-v2'  # 模型名称
encoder_device = 'cpu'              # 运行设备

# 生成模型配置
generator_model = 'gpt2'            # 模型名称
generator_device = 'cuda'           # 运行设备

# 状态管理配置
state_fusion_alpha = 0.7            # 新状态权重 (0~1)
state_decay_rate = 0.95             # 衰减率 (0~1)

# 生成参数
max_length = 100                    # 最大生成长度
temperature = 0.8                   # 温度 (0.1~2.0)
top_p = 0.9                         # nucleus sampling
top_k = 50                          # top-k sampling
```

### 修改配置

**方法1：命令行参数**

```bash
python main.py --temperature 0.7 --top-k 30 --interactive
```

**方法2：环境变量**

```bash
# Windows
set EMOVAR_TEMPERATURE=0.7
set EMOVAR_TOP_K=30

# Linux/macOS
export EMOVAR_TEMPERATURE=0.7
export EMOVAR_TOP_K=30
```

---

## 🐛 常见问题

### Q1: 安装很慢怎么办？

**A**: 使用国内镜像源：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q2: 模型下载很慢？

**A**: 使用 HuggingFace 国内镜像：

```bash
# Windows
set HF_ENDPOINT=https://hf-mirror.com

# Linux/macOS
export HF_ENDPOINT=https://hf-mirror.com
```

### Q3: 内存不足？

**A**: 使用更小的模型或CPU运行：

```bash
python main.py --generator-model gpt2 --device cpu
```

### Q4: 如何重置状态？

**A**: 交互模式输入 `/reset` 命令。

### Q5: 如何换用其他模型？

**A**: 使用 `--encoder-model` 和 `--generator-model` 参数。

---

## 💡 Python API 示例

```python
from config import Config
from situation_encoder import SituationEncoder
from infinite_state import InfiniteState
from model_injector import ModelInjector

# 初始化
encoder = SituationEncoder()
state = InfiniteState(dim=encoder.embedding_dim)
generator = ModelInjector()

# 处理情境
situation = "今天阳光明媚，鸟儿在歌唱"
vec = encoder.encode(situation)
state.update(vec, source=situation)

# 生成文本
prompt = "此刻的感受"
result = generator.generate(prompt, state.vector)
print(result)
```

---

## 📦 项目文件说明

```
EmoVar/
├── config.py              # 全局配置管理
├── situation_encoder.py   # 情境编码器（384维）
├── infinite_state.py      # 状态管理（加权融合）
├── model_injector.py      # 模型注入（prompt拼接）
├── data_loader.py         # TXT数据加载
├── main.py                # 主程序入口
├── requirements.txt       # 依赖清单（一键安装）
├── README.md              # 使用说明（本文件）
└── USAGE.md               # 详细手册
```

---

## 🎓 技术原理

### 情境编码

使用 `sentence-transformers` 将文本编码为384维连续向量，保留语义和情感信息。

### 状态融合

```
新状态 = α × 新情境向量 + (1-α) × 当前状态
```

- α = 0.7: 新情境占70%权重
- 历史状态逐步衰减，实现"记忆消退"

### 情感注入

将384维向量转换为自然语言描述：

```
[情感状态: 情感适中，偏向积极，情绪稳定]
```

拼接到 prompt 前缀，引导生成风格。

---

## 📄 许可证

本项目采用 MIT 许可证，自由使用和修改。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📮 联系方式

如有问题请在项目 Issues 中反馈。

---

**开始使用：**

```bash
pip install -r requirements.txt && python main.py --interactive
```

**享受情感化生成的乐趣！ 🎉**
