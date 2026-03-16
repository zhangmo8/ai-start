# 模型工程学习路线总入口

这套文档是给“前端转模型工程师，并且要从 0 做出自己的小模型”的长期学习系统。

- 学习总时长：36 个主题周 / 252 个学习日
- 计划起始日期：2026-03-13
- 预计完成日期：2027-03-01
- 建议强度：每周 10-15 小时
- 节奏设计：工作日学习，周六周日固定休息
- `Week XX` 表示 7 个学习日的主题块，不强行绑定自然周
- 当前写入时间点：2026-03-16
- 下一次应从 [Day 003](days/day003.md) 开始（2026-03-17）

## 先看哪些文件

- [PROGRESS.md](PROGRESS.md)：当前进度、今天是哪一天、下一步做什么
- [ROADMAP.md](ROADMAP.md)：完整路线图、阶段目标、周次安排
- [AI_HANDOFF.md](AI_HANDOFF.md)：给下一个 AI 会话的接力说明
- [SESSION_LOG.md](SESSION_LOG.md)：每次学习后的更新记录
- [resources.md](resources.md)：总资料索引

## 阶段入口

- [阶段 1 - 基础层](phases/phase1.md)
- [阶段 2 - 模型层](phases/phase2.md)
- [阶段 3 - 推理与系统层](phases/phase3.md)
- [阶段 4 - 开源模型适配层](phases/phase4.md)
- [阶段 5 - 评测与作品集层](phases/phase5.md)

## 周入口

- [Week 01 - Python 语法与运行时](weeks/week01.md)
- [Week 02 - Python 工程基础](weeks/week02.md)
- [Week 03 - 线性代数与 NumPy](weeks/week03.md)
- [Week 04 - 概率、Softmax、交叉熵与梯度直觉](weeks/week04.md)
- [Week 05 - PyTorch 张量与自动求导](weeks/week05.md)
- [Week 06 - 训练循环、数据管道与调试](weeks/week06.md)
- [Week 07 - 文本、语料与预处理](weeks/week07.md)
- [Week 08 - Tokenizer 基础与子词思想](weeks/week08.md)
- [Week 09 - 语言模型目标与困惑度](weeks/week09.md)
- [Week 10 - Embedding 与位置信息](weeks/week10.md)
- [Week 11 - Self-Attention 与 Q/K/V](weeks/week11.md)
- [Week 12 - Multi-Head、FFN、Residual、LayerNorm](weeks/week12.md)
- [Week 13 - Decoder-Only 架构](weeks/week13.md)
- [Week 14 - 训练你自己的小 Transformer v1](weeks/week14.md)
- [Week 15 - 生成策略与输出行为](weeks/week15.md)
- [Week 16 - 评测、回归与失败分析](weeks/week16.md)
- [Week 17 - 数据过滤、去重与语料质量](weeks/week17.md)
- [Week 18 - 模型规模、数据量与优化直觉](weeks/week18.md)
- [Week 19 - 推理基础与 checkpoint 载入](weeks/week19.md)
- [Week 20 - 上下文窗口与消息打包](weeks/week20.md)
- [Week 21 - Structured Output 与 Tool Calling](weeks/week21.md)
- [Week 22 - Prefill、Decode 与 KV Cache](weeks/week22.md)
- [Week 23 - 本地模型生态、GGUF 与 llama.cpp](weeks/week23.md)
- [Week 24 - 性能、延迟、吞吐与内存预算](weeks/week24.md)
- [Week 25 - 把模型包装成 API](weeks/week25.md)
- [Week 26 - MCP、Skill 与 Agent 边界](weeks/week26.md)
- [Week 27 - 开源模型生态与模型卡](weeks/week27.md)
- [Week 28 - 阅读开源 Transformer 实现](weeks/week28.md)
- [Week 29 - Instruction Tuning 与聊天数据格式](weeks/week29.md)
- [Week 30 - LoRA 与 PEFT](weeks/week30.md)
- [Week 31 - QLoRA 与低资源适配](weeks/week31.md)
- [Week 32 - 蒸馏、过滤与安全样本](weeks/week32.md)
- [Week 33 - 评测体系与回归集设计](weeks/week33.md)
- [Week 34 - 自己的模型 vs 开源模型](weeks/week34.md)
- [Week 35 - 技术写作、架构图与讲解能力](weeks/week35.md)
- [Week 36 - 总复盘与下一个 90 天](weeks/week36.md)

## 使用规则

- 如果你按计划推进，Day 001 对应 2026-03-13。
- 如果你中断了几天，不要按日历跳到后面的 day 文件，应该按 `PROGRESS.md` 中的 `当前学习日` 继续。
- 每学完一天，更新 `PROGRESS.md` 和 `SESSION_LOG.md`。
- 下一个 AI 会话不要依赖聊天上下文，直接读这几个文件即可接力。
