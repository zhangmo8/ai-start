# Day 17 - Multi-Head Attention 与 FFN

今天学什么：
- multi-head 的作用
- FFN 在 transformer block 中的职责
- 为什么 attention 后面还要 FFN

重点理解：
- 多头不是为了炫技，而是让模型从不同子空间看关系
- FFN 不是可有可无，它负责非线性变换和特征重组

去哪里学：
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- torch.nn.Transformer: https://docs.pytorch.org/docs/stable/generated/torch.nn.Transformer.html

今天的输出：
- 写 1 页笔记，对比 self-attention 和 FFN 的职责

完成标准：
- 你知道为什么一个 block 不只是 attention
