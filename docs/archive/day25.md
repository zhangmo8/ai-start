# Day 25 - 本地模型生态：llama.cpp 与轻量推理

今天学什么：
- 本地推理为什么常用轻量 runtime
- checkpoint、tokenizer、runtime 的关系
- 量化模型为什么更适合本地

重点理解：
- “本地跑模型”不是只会点开一个 app，而是知道模型文件、推理框架、量化和上下文之间的关系

去哪里学：
- llama.cpp 官方仓库: https://github.com/ggerganov/llama.cpp
- Text Generation Docs: https://huggingface.co/docs/transformers/en/main_classes/text_generation

今天的输出：
- 写 1 页笔记，解释“模型文件、tokenizer、runtime 为何必须对齐”

完成标准：
- 你知道为什么本地推理常常优先选小模型和量化模型
