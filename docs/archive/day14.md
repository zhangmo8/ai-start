# Day 14 - 语言模型训练目标

今天学什么：
- next-token prediction
- teacher forcing 的基本直觉
- perplexity 是什么

重点理解：
- 大语言模型最底层的训练目标并不神秘，就是预测下一个 token
- 聊天、工具调用、结构化输出，本质上都建立在这个目标上

去哪里学：
- Transformers Perplexity Docs: https://huggingface.co/docs/transformers/en/perplexity
- PyTorch CrossEntropyLoss: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html

今天的输出：
- 写 1 页笔记，标题叫“为什么 next-token prediction 能长出复杂能力”

完成标准：
- 你知道 loss、perplexity 和生成能力之间的大致关系
