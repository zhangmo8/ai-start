# Day 19 - Context Window、Mask、Batching

今天学什么：
- context window
- 序列长度
- padding / truncation 的意义
- mask 如何影响训练

重点理解：
- 模型不是无限记忆，context 是有限预算
- 训练和推理中的长度设计会直接影响成本和效果

去哪里学：
- Transformers Perplexity Docs: https://huggingface.co/docs/transformers/en/perplexity
- Attention Is All You Need: https://arxiv.org/abs/1706.03762

今天的输出：
- 写 1 页笔记，解释“为什么长上下文更贵”

完成标准：
- 你知道 context length 和训练成本、推理成本的关系
