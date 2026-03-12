# Day 18 - Residual、LayerNorm、Decoder-Only

今天学什么：
- residual connection
- layer normalization
- decoder-only 结构为什么适合生成

重点理解：
- 现代 LLM 主要是 decoder-only，不是完整 encoder-decoder
- residual 和 norm 直接关系到训练稳定性

去哪里学：
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- Chat Templates Docs: https://huggingface.co/docs/transformers/en/chat_templating

今天的输出：
- 写 1 页笔记，解释“为什么聊天模型本质上仍然是 causal LM”

完成标准：
- 你能说清 decoder-only 为什么适合 next-token generation
