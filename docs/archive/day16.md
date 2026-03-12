# Day 16 - Self-Attention 与 Q/K/V

今天学什么：
- Query、Key、Value
- attention score
- softmax over attention weights
- causal mask 的作用

重点理解：
- self-attention 的本质是“让 token 看别的 token”
- causal mask 保证语言模型不能偷看未来

去哪里学：
- Attention Is All You Need: https://arxiv.org/abs/1706.03762

今天的输出：
- 写 1 页笔记，解释 Q、K、V 各自扮演什么角色
- 画出 attention score 矩阵示意图

完成标准：
- 你能解释为什么 attention 里要有三个投影而不是一个
