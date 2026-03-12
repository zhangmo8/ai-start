# 给下一个 AI 会话的接力说明

如果你是新的 AI 上下文，请按以下顺序读取：

1. `docs/PROGRESS.md`
2. `docs/SESSION_LOG.md`
3. 当前学习日文件，例如 `docs/days/day001.md`
4. 如有需要，再看对应 `docs/weeks/weekXX.md` 和 `docs/phases/phaseX.md`

## 你的工作方式

- 先确认用户上次实际完成到了哪一天。
- 以 `PROGRESS.md` 的“最后完成的学习日”为主，不以自然日期为主。
- 如果用户没完成当天内容，继续帮助他完成当前 day 文件，不要自动跳到下一天。
- 每次学习结束后，建议用户把今天的收获、卡点、下一步写进 `SESSION_LOG.md`。
- 如果要继续细化内容，优先补充当前 day 文件对应的讲解、术语解释、论文导读、笔记模板。

## 你应该维护的文件

- `docs/PROGRESS.md`：更新当前 day、最后完成 day、状态
- `docs/progress.json`：同步更新机器可读状态
- `docs/SESSION_LOG.md`：追加本次学习记录

## 这套路线的目标边界

- 目标是成为模型工程师，不是纯 API 工程师。
- 路线覆盖：自己的小模型、推理、评测、MCP/agent 接入、开源模型理解、LoRA/QLoRA、蒸馏、过滤。
- 默认机器资源有限，所以前期以“小模型 + 深理解 + 强文档化”为主。
