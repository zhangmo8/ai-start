from __future__ import annotations

"""
Day 017 补充 demo：shape 和 broadcasting

根据 result/day017_beginner_guide.md 编写
运行：python3 test/day017_shape_broadcasting.py
"""

import numpy as np


def title(text: str) -> None:
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}")


def show(name: str, arr: np.ndarray, meaning: str = "") -> None:
    print(f"\n{name}:")
    print(arr)
    print(f"shape = {arr.shape}")
    if meaning:
        print(f"→ {meaning}")


def demo_shape_不是数字游戏() -> None:
    title("1. Shape 不是数字游戏")

    scores = np.array([
        [90, 85, 88],
        [76, 92, 81]
    ])

    show("scores", scores)
    print("不是只记 (2, 3)")
    print("要翻译成：2 个学生，每个学生 3 门成绩")


def demo_broadcasting_最简单例子() -> None:
    title("2. Broadcasting：shape 不同也能算")

    scores = np.array([
        [90, 85, 88],
        [76, 92, 81]
    ])

    bonus_per_subject = np.array([5, 0, 2])       # shape = (3,)
    extra_per_student = np.array([[3], [1]])      # shape = (2, 1)

    print("\n先猜：scores + bonus_per_subject 是按哪一维加？")
    print("再猜：scores + extra_per_student 是按哪一维加？\n")

    show("scores", scores, "2 个学生，3 门成绩")
    show("bonus_per_subject", bonus_per_subject, "每门课分别加 5, 0, 2 分")
    show("scores + bonus_per_subject", scores + bonus_per_subject, "同一组加分，给每一行都加一遍")

    show("extra_per_student", extra_per_student, "每个学生整体再加 3 分或 1 分")
    show("scores + extra_per_student", scores + extra_per_student, "每个学生自己的加分，广播到这一行的每一列")


def demo_broadcasting_规则() -> None:
    title("3. 广播规则（从右往左看）")

    print("""
    规则只有 3 条：
    1. 一样大 → 可以对齐
    2. 其中一个是 1 → 可以扩展
    3. 其他情况 → 不行
    """)

    cases = [
        ("(2, 3) 和 (3,)", "可以 ✓", "(3,) 变成 (1,3) 再变成 (2,3)"),
        ("(2, 3) 和 (1, 3)", "可以 ✓", "1 被扩展成 2"),
        ("(2, 3) 和 (2, 1)", "可以 ✓", "1 被扩展成 3"),
        ("(2, 3) 和 (2,)", "不行 ✗", "从右看：(3,) vs ()，不兼容"),
        ("(3, 4) 和 (5, 6)", "不行 ✗", "3≠5 且都不是 1"),
        ("(2, 3) 和 (3, 2)", "不行 ✗", "从右看：3≠2 且都不是 1"),
    ]

    for s1, s2, reason in cases:
        print(f"  {s1} + {s2} → {s2}  {reason}")


def demo_误区澄清() -> None:
    title("4. 常见误区澄清")

    print("""
    误区 1：广播就是自动瞎补
    → 不对！广播有规则，不是乱补

    误区 2：只要维度不同就不能算
    → 不对！满足规则就能算

    误区 3：广播会改变原数组 shape
    → 不对！原数组 shape 不变，只是运算时临时对齐
    """)

    a = np.array([[1, 2, 3]])
    b = np.array([10, 20, 30])
    result = a + b

    show("a", a, "shape 不变")
    show("b", b, "shape 不变")
    show("a + b", result, "只是运算时临时对齐")


def demo_神经网络中的应用() -> None:
    title("5. 模型中的 broadcasting")

    # 线性层
    x = np.random.randn(32, 128)   # 32 个样本，128 维
    w = np.random.randn(128, 64)   # 128 维 → 64 维
    b = np.random.randn(64)         # 偏置 shape = (64,)

    output = x @ w + b
    show("输入 x", x, "32 个样本")
    show("偏置 b", b, "shape = (64,)")
    show("x @ w + b", output, f"b 自动广播到每个样本，shape = {output.shape}")


def quiz() -> None:
    title("6. 自测：你能答对吗？")

    questions = [
        "shape=(2, 3) 怎么读？",
        "(2, 3) 和 (3,) 为什么能相加？",
        "广播最核心的规则是什么？",
    ]

    answers = [
        "2 个对象，每个对象 3 个东西（不是 2 行 3 列！要翻译成现实含义）",
        "从右往左：(3,) 对上 (3,)，所以能对齐；(3,) 复制到每一行",
        "从右往左看，一样大可以，1 可以扩展，其他不行",
    ]

    for i, (q, a) in enumerate(zip(questions, answers), 1):
        print(f"\n题 {i}：{q}")
        print(f"答：{a}")


def main() -> None:
    print("Day 017 补充 demo：shape 和 broadcasting")
    demo_shape_不是数字游戏()
    demo_broadcasting_最简单例子()
    demo_broadcasting_规则()
    demo_误区澄清()
    demo_神经网络中的应用()
    quiz()


if __name__ == "__main__":
    main()
