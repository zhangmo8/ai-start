# Day 27 - Tool Calling 与结构化输出

今天学什么：
- 模型为什么需要结构化输出
- tool calling 的最小思想
- JSON 风格输出为什么重要

重点理解：
- agent 系统不是让模型“自己施法”，而是让模型先表达意图，再由外层执行
- 这会直接影响你以后怎么设计自己的小模型接口

去哪里学：
- Chat Templates Docs: https://huggingface.co/docs/transformers/en/chat_templating
- MCP Introduction: https://modelcontextprotocol.io/introduction

今天的输出：
- 写 1 页笔记，解释“tool calling 本质上是结构化意图输出”

完成标准：
- 你知道为什么 tool calling 需要清晰 schema
