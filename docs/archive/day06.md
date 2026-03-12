# Day 06 - 概率、Softmax、交叉熵

今天学什么：
- 概率分布
- logits 和概率的区别
- softmax 在做什么
- cross entropy 在做什么

重点理解：
- 语言模型最后不是直接输出文字，而是输出下一个 token 的分布
- cross entropy 是你理解语言模型训练目标的第一把钥匙

去哪里学：
- PyTorch CrossEntropyLoss: https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html
- PyTorch Softmax: https://docs.pytorch.org/docs/stable/generated/torch.nn.Softmax.html

今天的输出：
- 写 1 页笔记，解释“为什么模型最后输出的是 logits 而不是文字”

完成标准：
- 你能用自己的话解释 softmax 和 cross entropy 各自干什么
