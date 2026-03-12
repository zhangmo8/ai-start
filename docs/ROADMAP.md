# 全量学习路线图

## 目标

- 从 0 理解并做出一个小型语言模型
- 理解 tokenizer、Transformer、训练、生成、推理、量化、微调、蒸馏、过滤、评测
- 理解模型与 tool calling、agent、MCP、skill 的边界与接入方式
- 后续再用开源模型做对照理解，而不是一上来就只会调 API

## 阶段划分

- 阶段 1 `基础层`：Week 01 - Week 06，补齐 Python、数学和 PyTorch 最小基础，建立读懂模型代码的能力。
- 阶段 2 `模型层`：Week 07 - Week 18，从文本、tokenizer、Transformer 到训练与生成，打通从 0 做小模型的理论路线。
- 阶段 3 `推理与系统层`：Week 19 - Week 26，理解推理链路、服务化、本地模型、tool calling、MCP 与 agent 边界。
- 阶段 4 `开源模型适配层`：Week 27 - Week 32，通过开源模型理解 chat template、SFT、LoRA、QLoRA、蒸馏、过滤。
- 阶段 5 `评测与作品集层`：Week 33 - Week 36，对比自己的模型与开源模型，形成稳定评测体系和后续 90 天计划。

## 核心原则

- 先把结构和原理吃透，再逐步接近工程实现
- 每一天都必须有输出，哪怕只是一页笔记或一张结构图
- 每一周都要有复盘，否则学习会碎片化
- 实际进度以 `PROGRESS.md` 为准，不以聊天上下文为准

## 周次一览

- Week 01 `Python 语法与运行时`：2026-03-13 - 2026-03-19，建立 Python 的基本心智模型，能读懂脚本、模块和控制流。
- Week 02 `Python 工程基础`：2026-03-20 - 2026-03-26，理解函数、模块、类型注解、异常、路径、配置和日志。
- Week 03 `线性代数与 NumPy`：2026-03-27 - 2026-04-02，建立张量、shape、矩阵乘法和广播的直觉。
- Week 04 `概率、Softmax、交叉熵与梯度直觉`：2026-04-03 - 2026-04-09，理解语言模型为什么输出 logits，为什么训练目标常用交叉熵。
- Week 05 `PyTorch 张量与自动求导`：2026-04-10 - 2026-04-16，理解 tensor、autograd、nn.Module 的基础工作方式。
- Week 06 `训练循环、数据管道与调试`：2026-04-17 - 2026-04-23，理解 Dataset、DataLoader、optimizer、train/eval、checkpoint 的骨架。
- Week 07 `文本、语料与预处理`：2026-04-24 - 2026-04-30，理解原始文本进入模型前要经历的数据清洗与预处理。
- Week 08 `Tokenizer 基础与子词思想`：2026-05-01 - 2026-05-07，理解 token、vocab、special token、字符级与 BPE 的差异。
- Week 09 `语言模型目标与困惑度`：2026-05-08 - 2026-05-14，理解 next-token prediction、teacher forcing、perplexity。
- Week 10 `Embedding 与位置信息`：2026-05-15 - 2026-05-21，理解 token id 如何变成向量，以及模型如何感知顺序。
- Week 11 `Self-Attention 与 Q/K/V`：2026-05-22 - 2026-05-28，真正理解 attention score、Q/K/V 和 causal mask。
- Week 12 `Multi-Head、FFN、Residual、LayerNorm`：2026-05-29 - 2026-06-04，理解一个 Transformer block 里其余关键零件。
- Week 13 `Decoder-Only 架构`：2026-06-05 - 2026-06-11，理解为什么现代 LLM 多数采用 decoder-only。
- Week 14 `训练你自己的小 Transformer v1`：2026-06-12 - 2026-06-18，从理论视角理解一个小模型训练实验需要哪些超参数与监控项。
- Week 15 `生成策略与输出行为`：2026-06-19 - 2026-06-25，理解 greedy、temperature、top-k、top-p、repetition penalty。
- Week 16 `评测、回归与失败分析`：2026-06-26 - 2026-07-02，建立最小评测意识：loss、perplexity、人工样例和回归集。
- Week 17 `数据过滤、去重与语料质量`：2026-07-03 - 2026-07-09，理解过滤与去重对小模型质量的决定性影响。
- Week 18 `模型规模、数据量与优化直觉`：2026-07-10 - 2026-07-16，理解参数规模、上下文长度、数据量和收敛之间的平衡。
- Week 19 `推理基础与 checkpoint 载入`：2026-07-17 - 2026-07-23，从训练转入推理，理解 eval、no_grad、checkpoint 与 logits 生成。
- Week 20 `上下文窗口与消息打包`：2026-07-24 - 2026-07-30，理解 context window、截断、消息拼接、历史管理。
- Week 21 `Structured Output 与 Tool Calling`：2026-07-31 - 2026-08-06，理解模型如何输出结构化意图，再由外层系统执行工具。
- Week 22 `Prefill、Decode 与 KV Cache`：2026-08-07 - 2026-08-13，理解为什么首 token 慢、后续 token 快，以及 KV cache 的价值。
- Week 23 `本地模型生态、GGUF 与 llama.cpp`：2026-08-14 - 2026-08-20，理解本地模型文件、量化格式、runtime 之间的关系。
- Week 24 `性能、延迟、吞吐与内存预算`：2026-08-21 - 2026-08-27，理解 token/s、首 token 延迟、吞吐、内存占用这些工程指标。
- Week 25 `把模型包装成 API`：2026-08-28 - 2026-09-03，理解 generate/chat/tool-call 这类接口为什么存在，以及各自的职责。
- Week 26 `MCP、Skill 与 Agent 边界`：2026-09-04 - 2026-09-10，理解模型、工具、MCP server、skill router 之间的边界。
- Week 27 `开源模型生态与模型卡`：2026-09-11 - 2026-09-17，理解 Hugging Face Hub、model card、checkpoint、license 的基本生态。
- Week 28 `阅读开源 Transformer 实现`：2026-09-18 - 2026-09-24，开始用源码视角理解 tokenizer、model、generation 三层。
- Week 29 `Instruction Tuning 与聊天数据格式`：2026-09-25 - 2026-10-01，理解 SFT、instruction 数据格式、chat template 和对齐的关系。
- Week 30 `LoRA 与 PEFT`：2026-10-02 - 2026-10-08，理解参数高效微调的核心思想和适用边界。
- Week 31 `QLoRA 与低资源适配`：2026-10-09 - 2026-10-15，理解量化与微调如何结合，以及资源受限场景的关键折中。
- Week 32 `蒸馏、过滤与安全样本`：2026-10-16 - 2026-10-22，理解 teacher-student、数据过滤和安全样本的最小框架。
- Week 33 `评测体系与回归集设计`：2026-10-23 - 2026-10-29，建立一套能持续比较模型版本的评测体系。
- Week 34 `自己的模型 vs 开源模型`：2026-10-30 - 2026-11-05，把自己的模型和开源模型放到同一评价维度上比较。
- Week 35 `技术写作、架构图与讲解能力`：2026-11-06 - 2026-11-12，把你学到的内容输出成可复用的技术文档和图示。
- Week 36 `总复盘与下一个 90 天`：2026-11-13 - 2026-11-19，回顾 36 周路线，整理成果、盲点和下一阶段目标。
