# Day 11 - 文本为什么要先变成 Token

今天学什么：
- token 的概念
- token 和 word 的区别
- vocab 的概念
- special tokens 的意义

重点理解：
- 模型从来不直接“理解文字”，模型处理的是 token id
- tokenizer 设计会深刻影响模型表达能力和训练效率

去哪里学：
- Hugging Face Tokenizers Docs: https://huggingface.co/docs/tokenizers/en/index
- SentencePiece 官方仓库: https://github.com/google/sentencepiece

今天的输出：
- 写 1 页笔记，标题叫“为什么模型先看 token 再看文本”

完成标准：
- 你知道 vocab、BOS、EOS、PAD 这些词分别是什么意思
