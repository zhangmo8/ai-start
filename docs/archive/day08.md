# Day 08 - nn.Module 与模型对象

今天学什么：
- `nn.Module`
- `forward`
- layer 的概念
- 参数和 buffer 的区别

重点理解：
- 以后无论是 MLP、Attention 还是 Transformer，都是 `nn.Module`
- 你必须先适应“模型是对象，训练是对象之间组合”的代码风格

去哪里学：
- Build Model Tutorial: https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html
- nn.Module 官方文档: https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html

今天的输出：
- 写 1 页笔记，解释“为什么模型通常写成类”

完成标准：
- 你能读懂一个最小的 `nn.Module` 模型类
