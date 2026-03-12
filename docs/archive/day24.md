# Day 24 - 推理链路：Prefill、Decode、KV Cache

今天学什么：
- prefill 和 decode 的区别
- KV cache 的意义
- 为什么首 token 慢、后续 token 快

重点理解：
- 推理不是一次性算完，而是分阶段进行
- 这部分是你从“懂模型结构”走向“懂模型系统”的分水岭

去哪里学：
- Transformers Cache Explanation: https://huggingface.co/docs/transformers/en/cache_explanation
- Text Generation Docs: https://huggingface.co/docs/transformers/en/main_classes/text_generation

今天的输出：
- 写 1 页笔记，标题叫“为什么长对话会越来越贵”

完成标准：
- 你能用自己的语言解释 KV cache 的价值
