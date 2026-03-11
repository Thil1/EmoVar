# 🧠 EmoVar: Let Emotions Speak for Themselves

[📖 中文版](README.md) | **English Version**

⚠️ **This is NOT another emotion recognition tool.**

I believe language can only vaguely express emotions. We should not label AI agents with emotional tags. Instead, we should let them exist continuously, evolve constantly, and perceive the world with a certain internal state — rather than following the pipeline of "input → emotion recognition → output."

---

## 📖 I. Problem and Answer

In 2025, I came across a news article about "AI energy" issues and had an idea: "How can I solve the problem of AI power consumption?" So I started discussing this with DeepSeek.

At that time, I asked a question:

> "Our brains think about so many things every day, why don't they get tired? Can the AI energy problem be approached in the same way?"

DeepSeek gave me an answer I will never forget:

### 🧠 Why is the human brain so energy-efficient?

The human brain weighs about 1.4 kg and consumes only 20 watts of power, yet it can handle extremely complex tasks. The secrets to its efficiency are:

- **Sparse and distributed computation**: The brain doesn't run at "full power" all the time. Only relevant neurons are activated (sparse activation), while AI large models typically mobilize all parameters for "dense computation."
- **Event-driven asynchronous processing**: Neurons transmit signals through pulses, firing only when necessary. In contrast, traditional AI chips use synchronous clock-driven architectures, generating a lot of invalid power consumption.
- **Integration of computation and storage**: The brain's computation (electrical signals) and memory (synaptic strength) are the same system, eliminating the need to move data back and forth between processors and memory, avoiding the "memory wall."
- **Continuous learning and energy adaptation**: The brain can consolidate memories and optimize connections through sleep, dynamically adapting to energy supply; whereas AI models are "solidified" after training.

As we chatted more, I asked: "Why doesn't AI have imagination?"

It told me:

### 🧩 Lack of real experience

Human "imagination" is rooted in direct experiences of the physical world, bodily sensations, and social interactions. AI's "knowledge" all comes from textual symbols. It cannot truly "understand" colors, pain, gravity, or the feeling of a hug. Therefore, its "imagination" is just a recombination of symbols, rather than experience-based mental simulation.

Later, I found a paper on arXiv titled "Simulating Human-like Daily Activities with Desire-driven Autonomy" and thought: I can build a world for AI and add "pleasure," "anger," and other emotional dimensions to it.

I asked OpenCode to help me build this "world." When the world was built, the "joy" and "anger" in it made me increasingly uneasy — it seemed like language can only vaguely express emotions. AI only knows those are a few characters but never knows what they mean.

Just like "fatherly love" and "motherly love" — some people feel care, while others experience domestic violence... And AI can never truly understand.

---

## 🔬 II. Conclusion and Evidence

My conclusion is:

**Language is a hard limitation.** The design goal of natural language is precision, unambiguity, and reproducibility, while the essence of emotion is vague, varies from person to person, and is non-reproducible. Using precise tools to express vague emotions is like using calipers to measure the shape of the wind. The same applies to artificial programming languages.

### Empirical evidence:

📜 **Meaning does not lie in the words themselves, but in the entire context of the speaker.**

- Ludwig Wittgenstein proposed in "Philosophical Investigations" that "**meaning is use**" — the meaning of a word lies in its specific usage in language.
- John R. Firth's famous saying: "**You shall know a word by the company it keeps**," emphasizing the decisive role of context in word meaning.
- Research paper: "Semantic Representations Are Updated Across the Lifespan Reflecting Diachronic Language Change"

🎭 **Psychological experiments have found** that when the literal meaning of a word is inconsistent with the speaker's emotional prosody, comprehension is impaired, indicating that emotional information is not in the word meaning.
- Research paper: "Literally or prosodically? Recognising emotional discourse in alexithymia"

🤖 **A research team from Shanghai Jiao Tong University found** that the way large language models learn emotions is essentially learning the context in which words appear, rather than the "emotional definition" of the words themselves.
- Research paper: "Zero-shot language learning: Can large language models learn emotions from context like humans?"

---

## 💡 III. My Solution

Since it's a "dead end," let's blaze a new trail.

I found that human babies are not born with specific emotions like "patriotism" or "homesickness," but with a set of **basic dimensions of emotion** (such as pleasure/displeasure, arousal/calmness). These are the "factory settings" of all living beings. Later experiences, culture, and education are mixed and named on top of these basic dimensions, eventually forming complex socialized emotions.

I believe emotions are formed by **"innate framework" + "acquired training."** We don't teach AI to "define" emotions. Instead, we give it a free internal state vector, allowing it to naturally express emotions in specific situations. This vector has no preset semantics, but it affects every sentence the model outputs. Users "experience" emotions from what the model says, rather than asking the model "what emotion are you feeling now."

We propose the concept of **"Infinite Variable Language"**: using continuous space (high-dimensional vectors) to express emotions, rather than discrete labels.

For example, "longing" can be expressed as a vector containing dimensions such as intensity, direction, temperature, and sense of time. Since creating a truly infinite variable language is too difficult, we can infinitely approach it.

---

## 🧪 IV. MVP Demonstration

We are not trying to create a perfect emotional agent, but rather evidence that the existing discrete label paradigm is wrong, and proof that continuous vector expression is possible.

### Implementation:

**Data**: Collect dozens of "genuine" emotional fragments from human creations such as novels, TV dramas, and TikTok comments (e.g., reflections after a breakup, joy of reunion). This data must be written by humans because AI-generated data lacks real emotional causal chains.

**Model**: Use MS-Swift from ModelScope to fine-tune a small open-source model (such as Qwen2.5-0.5B) to learn to output a multi-dimensional vector (such as pleasure, arousal) based on situational descriptions, or directly generate text that fits the situation.

**Comparison**: Run a traditional emotion classification model simultaneously, outputting probabilities of discrete labels. Display both side by side, allowing users to intuitively feel the difference between "labels" and "experience."

### Example:

**Input situation**: "The person you've secretly loved for three years tells you today that they're getting married."

**Traditional model output**:
```
Sadness: 0.9, Calmness: 0.1, Others: 0.0
```
(Can this express the complex emotion mixed with loss, blessing, and relief?)

**Our model output**:
```
Pleasure=-0.3, Arousal=0.5, Sense of time=-0.8, ...
```

The generated text might be:
> "Really... That's good."

(But the tone hides complex emotions that require the reader to experience.)

---

## 🔁 V. My Dissatisfaction with the MVP

My initial design loop was:

```
Input situation → Encoding → Update state → Generate response → Output
```

This process seems fine, but it has a fundamental flaw: **Emotions do not exist only "after processing the situation," but flow continuously throughout the entire conversation.**

I think the loop should be like this:

```
User input → Encoding → Update state
    ↓           ↓
    ← ← ← ← ← ← ← ← ← ←
             ↓
    Generate response (state changes continuously during the process)
             ↓
          Output
             ↓
(Waiting for next input, but state keeps "flowing")
```

### Key differences:

1. The state doesn't only change during "updates," but changes continuously throughout the generation process.
2. Every sentence generated affects the state in return (e.g., when talking about sad things, one becomes sadder).
3. The state itself has its own "life" (naturally decays over time, fluctuates randomly).

**There is still a gap between my ideas and the code.**

I hope someone can help improve this design.

---

## ⚠️ VI. Current Status

Due to my personal hardware limitations, the current MVP has not been fully tested, but the code framework is ready.

We sincerely invite developers with computing resources to verify together and explore this new direction.

My research direction may have shortcomings. Please feel free to offer your guidance!

---

## 🌟 VII. Why It's Worth Attention

**Paradigm Revolution**: I'm not patching up existing frameworks, but questioning the underlying logic of emotion computing. If the direction is right, this will be a paradigm shift from "recognition" to "experience."

**Intellectual Depth**: Our core ideas (emotions as innate framework + acquired training, language as a hard limitation, infinite variable language) are not wishful thinking, but are supported by cutting-edge research (such as APER models, emotional causal chain research, cultural linguistics research).

**Practical Value**: Future AI should not just be cold tools, but should be able to understand human emotions and even establish emotional connections with humans (but never for humanoid robots). Our framework provides a new way of thinking for this goal.

---

## 🚀 VIII. Next Steps

1. Improve data collection and annotation processes, and build high-quality high-context cultural emotion datasets.
2. Optimize the dynamic evolution mechanism of state vectors to make them closer to the fluidity of real emotions.
3. Explore the emergence of emotions in multi-agent social interactions.

---

## 🤝 IX. We Need You

If you are also troubled by the problem that "language is a cage for emotions," if you also believe that the current emotion computing path needs to be rethought, welcome to join us.

Whether you are a developer, researcher, or simply interested in this direction, you can:

⭐ **Star this project on GitHub.**

💬 **Submit an Issue**, sharing your ideas or discovered problems.

📝 **Contribute code, data, or documentation.**

We don't pursue numbers, only resonance of ideas. Let us pave the way for the next generation of emotional agents.

---

## 🙏 X. Acknowledgments

This project would not have been possible without the support of the following institutions, projects, and researchers (in no particular order):

- **NVIDIA**: Thanks for providing the API Key, giving me the opportunity to validate ideas in a real environment.
- **OpenCode Team**: Thanks for their powerful AI programming tools, which helped me generate a large amount of initial code framework.
- **DeepSeek**: Thanks for their large model and the paper "Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models (Engram)," which gave me deep inspiration about "memory lookup."
- **Beijing Institute for General Artificial Intelligence & Paper Authors**: Thanks for the research "Simulating Human-like Daily Activities with Desire-driven Autonomy (D2A)," which showed me the possibility of "desire-driven."
- **Wu Shiyu Team from Shanghai Jiao Tong University**: Thanks for their research "Zero-shot language learning: Can large language models learn emotions from context like humans?" providing empirical evidence for "language learning emotions."
- **University of Helsinki Related Research**: Thanks for their profound insights into "emotion construction."
- **Wittgenstein**: Thanks for his philosophical inspiration about "meaning is use" in "Philosophical Investigations."
- **John R. Firth**: Thanks for his famous saying "You shall know a word by the company it keeps."
- **Augustyn (2025)** and the authors of "Semantic Representations Are Updated Across the Lifespan Reflecting Diachronic Language Change."
- **Telli & Bilge (2024)** and the authors of "Literally or prosodically? Recognising emotional discourse in alexithymia."
- **ModelScope Community**: Thanks for providing free computing power and MS-Swift tools, making fine-tuning experiments possible.
- **Datawhale Community**: Thanks for their open-source tutorials "Hands-on Large Models" and "Happy-LLM," which helped me lay a practical foundation.
- **arXiv**: Thanks for this open preprint platform, allowing me to access cutting-edge papers.
- And all developers sharing knowledge and insights on GitHub, Zhihu, and Bilibili. Every discussion has benefited me greatly.

---

## 💬 Final Words

This project started with a question I had at age 14: If emotions cannot be defined by language, how should AI learn emotions?

After several years of thinking and practice, I realize the answer is not about letting AI learn to "define," but about letting AI learn to "experience."

The framework we built is just a beginning. It is rough and imperfect, but it represents a direction.

If you have also been inexplicably moved by a passage of text in the middle of the night, unable to explain that feeling with words —

Then you will understand what we are doing.

**Let us together create the ruler that can measure the wind.**

---

---

# 📚 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [📖 Project Introduction](#-project-introduction)
- [💻 Installation Guide](#-installation-guide)
- [🎯 Usage](#-usage)
- [🎬 Real Examples](#-real-examples)
- [🛠️ Advanced Options](#️-advanced-options)
- [📁 Data Format](#-data-format)
- [🔧 Module Testing](#-module-testing)
- [🧪 Interactive Demo](#-interactive-demo)
- [📚 Technical Architecture](#-technical-architecture)
- [⚙️ Configuration](#️-configuration)
- [🐛 FAQ](#-faq)
- [💡 Python API](#-python-api)
- [📦 Project Structure](#-project-structure)
- [🎓 Technical Principles](#-technical-principles)
- [⚠️ Ethical Use Statement](#️-ethical-use-statement)
- [📄 License](#-license)

---

---

# 🚀 Quick Start

## One-command installation and run

```bash
pip install -r requirements.txt && python main.py --interactive
```

**Estimated download**: ~600MB (on first run)
- `all-MiniLM-L6-v2`: ~90MB
- `gpt2`: ~500MB

---

# 📖 Project Introduction

EmoVar is an innovative emotional language generation system. It does not preset any emotion labels, but uses **continuous vectors** to represent the agent's internal emotional state.

**Core Idea**: Let users **experience emotions** from the generated text, rather than recognizing emotion categories.

---

# 💻 Installation Guide

### Prerequisites

- Python 3.8 or higher

### Install Dependencies

```bash
pip install -r requirements.txt
```

The installation process will automatically download:
- `sentence-transformers` (situation encoding)
- `transformers` (text generation)
- `torch` (deep learning framework)
- `numpy` (numerical computation)

### Verify Installation

```bash
python -c "import sentence_transformers; import transformers; import torch; import numpy; print('All dependencies installed')"
```

---

# 🎯 Usage

## Method 1: Interactive Mode (Recommended)

```bash
python main.py --interactive
```

After running, enter the interactive interface:

```
============================================================
EmoVar Interactive Mode
============================================================
Enter situation description, system will generate emotional text
Commands:
  /reset - Reset state
  /decay - Emotional decay
  /state - View current state
  /quit - Exit program
============================================================

Enter situation (or command): Today is sunny, birds are singing
Enter generation prompt (leave empty for none): My feelings right now

State: InfiniteState(dim=384, status=initialized, updates=1)
Generation: Warm sunshine spills into my heart, everything seems so beautiful...
```

## Method 2: Use Sample Data

```bash
python main.py --sample-data
```

The system will automatically create 10 sample situations and process them in batch.

## Method 3: Load from File

```bash
python main.py --input-file ./situations.txt --prompt "My feelings right now"
```

---

# 🎬 Real Examples

### Example 1: Morning Sunshine

**Input Situation**:
```
This morning, sunshine streamed through the gaps in the curtains, warm and gentle.
```

**State Vector Features** (first 5 dimensions):
```
[ 0.023, -0.156, 0.089, 0.234, -0.078, ... ]
```

**Generated Output**:
```
[Emotional State: Moderate emotion, leaning positive, emotionally stable]

My feelings right now:
Sunshine streams through the curtains, warm and gentle. Such a morning makes one feel peaceful and comfortable,
as if the whole world is slowly waking up. The mood involuntarily becomes light, as if caressed by this ray of sunshine.
```

---

### Example 2: Late Night Overtime

**Input Situation**:
```
2 AM, only me in the office, computer screen light reflecting on my face.
Deadline is in three hours.
```

**State Vector Features** (first 5 dimensions):
```
[ -0.189, 0.267, 0.145, -0.203, 0.312, ... ]
```

**Generated Output**:
```
[Emotional State: Moderate emotion, leaning reserved, emotionally volatile]

My feelings right now:
The screen light is a bit harsh, eyes already somewhat dry. Time passes minute by minute,
my mind feels like a tangled mess that can't be sorted out. Both anxious and somewhat numb,
don't know when this state will end...
```

**Note**: Continuous vectors have no labels like "anxious" or "tired"; emotions are experienced from the generated text.

---

### Example 3: State Change Comparison

**First Round Input**: "Received long-awaited admission notice"

**Second Round Input**: "Discovered tuition exceeds family budget"

**After State Fusion** (pleasure changes from positive to negative, but not completely disappeared):

```
[Emotional State: Moderate emotion, emotionally volatile]

My feelings right now:
Holding that paper in hand, mixed feelings. Should be a happy moment, but feel a heaviness instead.
The distance between dreams and reality is sometimes so close yet so far...
```

---

# 🛠️ Advanced Options

### Specify Models

```bash
# Use larger encoder
python main.py --encoder-model all-mpnet-base-v2

# Use GPT-2 medium model
python main.py --generator-model gpt2-medium

# Use other generation models
python main.py --generator-model microsoft/DialoGPT-medium
```

### GPU Acceleration

```bash
python main.py --device cuda --interactive
```

Requires NVIDIA GPU and CUDA support.

---

# 📁 Data Format

Create `situations.txt` (UTF-8 encoding):

```
Morning sunshine streams through the window
Stormy street, pedestrians hurrying to take shelter
Quiet library, only the sound of turning pages
Bustling market, vendors calling out one after another
Overlooking the sea of clouds from the mountaintop, feeling open-minded
```

**One situation per line, automatically processed in batch.**

---

# 🔧 Module Testing

### Test Situation Encoder

```bash
python situation_encoder.py
```

Outputs 384-dimensional vector representation.

### Test State Management

```bash
python infinite_state.py
```

Demonstrates state fusion and decay effects.

### Test Generation Model

```bash
python model_injector.py
```

Tests emotional text generation.

---

# 🧪 Interactive Demo

We provide `demo.ipynb` as an interactive demo. If you don't have Jupyter Notebook environment, you can use the following methods:

## Method 1: Convert to Python Script (Recommended)

```bash
# Install conversion tool
pip install nbconvert

# Convert to Python script
jupyter nbconvert --to script demo.ipynb

# Run script
python demo.py
```

## Method 2: Open directly in VS Code

1. Install VS Code
2. Install Jupyter extension (Python + Jupyter extensions)
3. Open `demo.ipynb` file directly to run

## Method 3: Google Colab (Online)

1. Visit [colab.research.google.com](https://colab.research.google.com)
2. Upload `demo.ipynb` file
3. Run online without local environment

## Method 4: Manual Copy

Open `demo.ipynb` file directly, copy content from code cells to new `.py` file and run.

**Note**: Need to install dependencies before running demo:

```bash
pip install -r requirements.txt
```

---

# 📚 Technical Architecture

```
Input situation text
    ↓
┌─────────────────────┐
│ SituationEncoder    │ Encode to 384-dimensional vector
│ (all-MiniLM-L6-v2)  │
└─────────────────────┘
    ↓
┌─────────────────────┐
│ InfiniteState       │ Weighted fusion of states
│ (Continuous emotion │ update / decay / reset
│  vector)            │
└─────────────────────┘
    ↓
┌─────────────────────┐
│ ModelInjector       │ Prompt concatenation injection
│ (gpt2)              │ Generate emotional text
└─────────────────────┘
    ↓
Output emotional language
```

---

# ⚙️ Configuration

### config.py Key Parameters

```python
# Encoder configuration
encoder_model = 'all-MiniLM-L6-v2'  # Model name
encoder_device = 'cpu'              # Device

# Generation model configuration - Auto-detect CUDA
generator_model = 'gpt2'            # Model name
generator_device = 'auto'           # Device (auto-detect: use CUDA if available, else CPU)

# State management configuration
state_fusion_alpha = 0.7            # New state weight (0~1)
state_decay_rate = 0.95             # Decay rate (0~1)

# Generation parameters
max_length = 100                    # Maximum generation length
temperature = 0.8                   # Temperature (0.1~2.0)
top_p = 0.9                         # nucleus sampling
top_k = 50                          # top-k sampling
```

### Command Line Arguments

```bash
python main.py --temperature 0.7 --top-k 30 --interactive
```

### Environment Variables

```bash
# Windows
set EMOVAR_TEMPERATURE=0.7
set EMOVAR_TOP_K=30

# Linux/macOS
export EMOVAR_TEMPERATURE=0.7
export EMOVAR_TOP_K=30
```

---

# 🐛 FAQ

### Q1: Installation is very slow?

**A**: Use domestic mirror source:

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q2: Model download is very slow?

**A**: Use HuggingFace domestic mirror:

```bash
# Windows
set HF_ENDPOINT=https://hf-mirror.com

# Linux/macOS
export HF_ENDPOINT=https://hf-mirror.com
```

### Q3: Out of memory?

**A**: Use smaller model or CPU:

```bash
python main.py --generator-model gpt2 --device cpu
```

### Q4: How to reset state?

**A**: Enter `/reset` command in interactive mode.

### Q5: How to switch models?

**A**: Use `--encoder-model` and `--generator-model` parameters.

---

# 💡 Python API

```python
from config import Config
from situation_encoder import SituationEncoder
from infinite_state import InfiniteState
from model_injector import ModelInjector

# Initialize
encoder = SituationEncoder()
state = InfiniteState(dim=encoder.embedding_dim)
generator = ModelInjector()

# Process situation
situation = "Today is sunny, birds are singing"
vec = encoder.encode(situation)
state.update(vec, source=situation)

# Generate text
prompt = "My feelings right now"
result = generator.generate(prompt, state.vector)
print(result)
```

---

# 📦 Project Structure

```
EmoVar/
├── config.py              # Global configuration
├── situation_encoder.py   # Situation encoder (384-dim)
├── infinite_state.py      # State management (weighted fusion)
├── model_injector.py      # Model injection (prompt concatenation)
├── data_loader.py         # TXT data loading
├── main.py                # Main entry
├── requirements.txt       # Dependencies (one-click install)
├── README.md              # Project docs (this file)
├── README_EN.md           # English version
├── DATA_ETHICS.md         # Data & ethics statement
├── Dockerfile             # Docker deployment
├── demo.ipynb             # Interactive demo
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD configuration
├── tests/
│   ├── __init__.py
│   └── test_infinite_state.py  # Unit tests
└── data/                  # Data directory (created at runtime)
    └── situations.txt     # Sample data
```

---

# 🎓 Technical Principles

### Situation Encoding

Use `sentence-transformers` to encode text into 384-dimensional continuous vectors, preserving semantic and emotional information.

### State Fusion

```
New state = α × new situation vector + (1-α) × current state
```

- α = 0.7: New situation accounts for 70% weight
- Historical states gradually decay, achieving "memory fade"

### Emotion Injection

Convert 384-dimensional vector to natural language description:

```
[Emotional State: Moderate emotion, leaning positive, emotionally stable]
```

Concatenate to prompt prefix to guide generation style.

---

# ⚠️ Ethical Use Statement

## Project Positioning

**EmoVar is an academic research and technology exploration project**, aiming to explore the possibility of expressing emotions with continuous vectors, rather than providing production-level emotion computing tools.

## Usage Restrictions

1. **Not for humanoid robots**: This project explicitly opposes using emotion generation technology for humanoid robots to avoid misleading users into thinking AI has real emotions.

2. **Not for emotion manipulation**: Prohibited from using this technology for any form of emotion manipulation, deception, or inducement (such as marketing brainwashing, emotional fraud, etc.).

3. **Not for medical diagnosis**: This system cannot replace professional mental health assessments and treatments.

4. **Clear user notification**: In any application scenario, users must be clearly informed that "this is AI-generated text and does not represent real emotions."

## Data Ethics

- This project uses public datasets and human-created content for research and demonstration
- For commercial or large-scale deployment, ensure data sources are legal and properly authorized
- Sensitive data should be de-identified

## Research Purpose

This project is committed to:
- Exploring paradigm shifts in emotion computing (from "recognition" to "experience")
- Verifying the feasibility of continuous vector expression of emotions
- Providing new research directions for next-generation emotional agents

**We believe the value of technology lies in enhancing human understanding, not replacing or manipulating.**

---

# 📄 License

This project uses MIT License, free to use and modify.

Issues and Pull Requests are welcome!

---

**Start using:**

```bash
pip install -r requirements.txt && python main.py --interactive
```

**Enjoy the fun of emotional generation! 🎉**
