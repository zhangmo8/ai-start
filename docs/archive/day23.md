# Day 23 - Chat Template 与指令格式

今天学什么：
- chat template 是什么
- role / content 结构
- system / user / assistant 的边界
- instruction tuning 的直觉

重点理解：
- 聊天模型本质还是 token continuation，只是输入格式更讲究
- 模型接不接 agent，和消息模板设计高度相关

去哪里学：
- Chat Templates Docs: https://huggingface.co/docs/transformers/en/chat_templating
- Self-Instruct: https://arxiv.org/abs/2212.10560

今天的输出：
- 写 1 页笔记，解释“chat 其实仍然是序列建模”

完成标准：
- 你知道 system prompt 为什么不是随便加一段字符串那么简单
