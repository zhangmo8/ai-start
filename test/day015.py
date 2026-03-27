from __future__ import annotations

"""
Day 015 - 线性代数与 NumPy / 总览与框架

这不是“公式课”，而是 Week 03 的地图课。
你需要先建立一个最小心智模型：

1. 数据不是乱堆的数字，而是按维度组织起来的结构。
2. 向量、矩阵、张量，本质上都是不同维度的数组。
3. shape 用来描述“每一维有多大”。
4. broadcasting 让某些不同 shape 的数组也能一起做逐元素运算。
5. 矩阵乘法会让 shape 发生规则化变化，这正是模型里线性层的基础。

运行方式：
    python3 test/day015.py
"""

import numpy as np


def show(title: str) -> None:
    print(f"\n=== {title} ===")


def describe(name: str, array: np.ndarray, meaning: str) -> None:
    print(f"{name}:")
    print(array)
    print(f"shape = {array.shape}, ndim = {array.ndim}")
    print(f"怎么理解: {meaning}")


def demo_1_vector_matrix_tensor() -> None:
    show("1. 向量、矩阵、张量到底是什么")

    scalar = np.array(7)
    vector = np.array([10, 20, 30])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    tensor = np.array(
        [
            [[1, 2], [3, 4], [5, 6]],
            [[7, 8], [9, 10], [11, 12]],
        ]
    )

    describe("标量 scalar", scalar, "0 维。就是一个单独的数。")
    describe("向量 vector", vector, "1 维。可以理解成一排数字。")
    describe("矩阵 matrix", matrix, "2 维。可以理解成一个表格：2 行 3 列。")
    describe(
        "张量 tensor",
        tensor,
        "3 维。可以理解成 2 个 3x2 的小表格叠在一起。",
    )

    print("\n一句话记忆：")
    print("维度越高，不是“更神秘”，只是数字按更多层次组织起来。")


def demo_2_shape_is_the_map() -> None:
    show("2. shape 为什么是最重要的阅读入口")

    student_scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    describe(
        "student_scores",
        student_scores,
        "shape (2, 3) 表示：2 个学生，每个学生有 3 门成绩。",
    )

    print("\n读 shape 的习惯：")
    print("- 不要只看数字本身，要先问“每一维代表谁”。")
    print("- (2, 3) 不是抽象符号，而是“2 个对象，每个对象 3 个特征”。")
    print("- 后面看模型代码时，经常会读成 batch x feature、batch x seq x hidden。")


def demo_3_broadcasting() -> None:
    show("3. broadcasting: 为什么不同 shape 有时也能相加")

    scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    bonus = np.array([5, 0, 2])

    describe("scores", scores, "2 个学生 x 3 门成绩")
    describe("bonus", bonus, "3 门课各自加多少分")

    final_scores = scores + bonus
    describe(
        "scores + bonus",
        final_scores,
        "bonus 的 shape 是 (3,)，会被当成“每一行都加同一组 3 个加分”。",
    )

    print("\n这就是 broadcasting 的直觉：")
    print("不是随便乱补，而是 NumPy 发现末尾维度能对齐，就自动扩展。")

    wrong_bonus = np.array([1, 2])
    print("\n如果 shape 对不上，就会报错：")
    try:
        print(scores + wrong_bonus)
    except ValueError as exc:
        print("scores + wrong_bonus ->", repr(exc))


def demo_4_matrix_multiplication() -> None:
    show("4. 矩阵乘法: 为什么它会改变 shape")

    x = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )
    w = np.array(
        [
            [1, 0],
            [0, 1],
            [1, 1],
        ]
    )

    describe("输入 x", x, "shape (2, 3): 2 条样本，每条样本 3 个特征")
    describe("权重 w", w, "shape (3, 2): 把 3 维特征映射到 2 维输出")

    y = x @ w
    describe("输出 y = x @ w", y, "shape (2, 2): 样本数保留，特征维从 3 变成 2")

    print("\n矩阵乘法最关键的一句：")
    print("(2, 3) @ (3, 2) -> (2, 2)")
    print("中间那个 3 必须对齐；它像是“被消费掉”的维度。")


def demo_5_model_view() -> None:
    show("5. 把前面几件事串成模型里的数据流")

    x = np.array(
        [
            [0.2, 0.8, 1.0],
            [1.2, 0.4, 0.6],
        ]
    )
    w = np.array(
        [
            [0.5, 0.1, -0.2, 0.7],
            [0.3, 0.9, 0.4, -0.5],
            [0.8, -0.3, 0.2, 0.1],
        ]
    )
    b = np.array([0.1, 0.1, 0.1, 0.1])

    describe("输入 x", x, "shape (2, 3): batch=2, feature=3")
    describe("权重 w", w, "shape (3, 4): 把 3 维输入投影到 4 维")
    describe("偏置 b", b, "shape (4,): 1 组长度为 4 的偏置，会广播到每条样本")

    linear_output = x @ w + b
    describe(
        "线性层输出 x @ w + b",
        linear_output,
        "先做矩阵乘法得到 (2, 4)，再把 b 广播到每一行。",
    )

    print("\n这一步已经非常像神经网络里的线性层了：")
    print("- x 负责提供输入数据")
    print("- w 负责决定如何混合特征")
    print("- b 负责给每个输出维度一个固定偏移")
    print("- shape 负责保证这一切能正确发生")


def summary() -> None:
    show("6. 今天你真正要带走的东西")
    print("1. Week 03 的重点不是背 API，而是建立“数据形状与运算”的直觉。")
    print("2. 向量、矩阵、张量只是不同维度的数组。")
    print("3. 看数组先看 shape，再问每一维代表什么。")
    print("4. broadcasting 解决的是逐元素运算时的自动对齐问题。")
    print("5. 矩阵乘法解决的是特征变换问题，也是模型线性层的基础。")

    print("\n如果你能复述下面这句话，就算今天学到了核心：")
    print(
        "模型代码里的数字不是乱飘的，"
        "它们总是以某种 shape 的张量存在，并通过广播和矩阵乘法不断变形。"
    )


def main() -> None:
    print("Day 015 demo: 用代码建立 Week 03 的全局地图")
    demo_1_vector_matrix_tensor()
    demo_2_shape_is_the_map()
    demo_3_broadcasting()
    demo_4_matrix_multiplication()
    demo_5_model_view()
    summary()


if __name__ == "__main__":
    main()
