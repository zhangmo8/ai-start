# Day 13 - BPE 与子词切分

今天学什么：
- 为什么字符级不够
- 为什么整词级也不够
- BPE / 子词切分在解决什么问题

重点理解：
- tokenizer 不是简单切字符串，它是模型能力与效率的前置设计
- 你后面看开源模型时，tokenizer 差异常常很关键

去哪里学：
- BPE 论文: https://arxiv.org/abs/1508.07909
- SentencePiece 官方仓库: https://github.com/google/sentencepiece

今天的输出：
- 写 1 页笔记，对比“字符级 / 词级 / 子词级”三种方式

完成标准：
- 你知道为什么现代 LLM 普遍不用纯字符级 tokenizer
