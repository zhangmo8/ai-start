from __future__ import annotations

"""
Week 03 学习 demo：线性代数与 NumPy

运行：
    python3 test/week03_learning_pack.py
"""

import numpy as np


def title(text: str) -> None:
    print(f"\n=== {text} ===")


def show(name: str, arr: np.ndarray, meaning: str) -> None:
    print(f"{name}:")
    print(arr)
    print(f"shape={arr.shape}, ndim={arr.ndim}")
    print(f"解释：{meaning}")


def demo_array_types() -> None:
    title("1. 标量、向量、矩阵、张量")

    scalar = np.array(7)
    vector = np.array([10, 20, 30])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    tensor = np.arange(24).reshape(2, 3, 4)

    show("scalar", scalar, "一个单独的数，0 维。")
    show("vector", vector, "一排数，1 维。")
    show("matrix", matrix, "二维表格，2 行 3 列。")
    show("tensor", tensor, "三维数组，2 组 3x4 表格。")


def demo_shape_reading() -> None:
    title("2. 先读 shape，再读内容")

    students = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    batch_tokens = np.arange(24).reshape(2, 3, 4)

    show("students", students, "2 个学生，每个学生 3 门成绩。")
    show("batch_tokens", batch_tokens, "2 条样本，每条 3 个 token，每个 token 4 维。")


def demo_slice_and_transpose() -> None:
    title("3. 切片、索引、转置")

    cube = np.arange(24).reshape(2, 3, 4)
    show("cube", cube, "一个 3 维张量。")

    first_block = cube[0]
    second_row_all = cube[:, 1]
    last_channel = cube[:, :, 2]
    swapped = cube.transpose(1, 0, 2)

    show("cube[0]", first_block, "取第 1 个大块，shape 少了一维。")
    show("cube[:, 1]", second_row_all, "取每个大块里的第 2 行。")
    show("cube[:, :, 2]", last_channel, "取每个位置的第 3 个数。")
    show("cube.transpose(1, 0, 2)", swapped, "交换前两维，shape 变成 (3, 2, 4)。")

    print("记忆法：切片会缩小或保留维度，转置只是重新排列维度顺序。")


def demo_broadcasting() -> None:
    title("4. broadcasting")

    scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    bonus_per_subject = np.array([5, 0, 2])
    extra_per_student = np.array([[3], [1]])

    show("scores", scores, "2 个学生 x 3 门课。")
    show("bonus_per_subject", bonus_per_subject, "每门课统一加分。")
    show("extra_per_student", extra_per_student, "每个学生统一再加分。")

    show("scores + bonus_per_subject", scores + bonus_per_subject, "按列广播到每一行。")
    show("scores + extra_per_student", scores + extra_per_student, "按行广播到每一列。")

    try:
        print(scores + np.array([1, 2]))
    except ValueError as exc:
        print(f"错误示例：{exc}")

    print("广播口诀：从最后一维往前看，能对齐、能补 1，才行。")


def demo_matrix_multiplication() -> None:
    title("5. 矩阵乘法")

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

    show("x", x, "2 条样本，每条样本 3 个特征。")
    show("w", w, "把 3 个输入特征映射成 2 个输出特征。")
    show("x @ w", x @ w, "(2, 3) @ (3, 2) -> (2, 2)")

    print("矩阵乘法口诀：左边最后一维 = 右边第一维，外面的维度留下来。")


def demo_linear_layer_view() -> None:
    title("6. 模型里的线性层长什么样")

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
    y = x @ w + b

    show("x", x, "batch=2, feature=3")
    show("w", w, "3 -> 4 的特征变换")
    show("b", b, "长度 4 的偏置，会广播。")
    show("y = x @ w + b", y, "线性层输出，shape=(2, 4)。")

    print("这就是你以后在神经网络里经常看到的基本形态。")


def summary() -> None:
    title("7. 你今天要带走的结论")
    print("1. 向量、矩阵、张量只是不同维度的数组。")
    print("2. 先读 shape，再问每一维代表什么。")
    print("3. 切片、转置、reshape 会改变你看到数据的方式。")
    print("4. 广播解决逐元素运算的对齐问题。")
    print("5. 矩阵乘法解决特征变换问题。")


def main() -> None:
    print("Week 03 学习 demo")
    demo_array_types()
    demo_shape_reading()
    demo_slice_and_transpose()
    demo_broadcasting()
    demo_matrix_multiplication()
    demo_linear_layer_view()
    summary()


if __name__ == "__main__":
    main()
