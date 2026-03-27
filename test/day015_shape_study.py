from __future__ import annotations

"""
Day 015 补充 demo：用“猜 shape -> 看结果 -> 听解释”的方式学懂

运行：
    python3 test/day015_shape_study.py
"""

import numpy as np


def title(text: str) -> None:
    print(f"\n=== {text} ===")


def show_array(name: str, arr: np.ndarray, meaning: str) -> None:
    print(f"{name}:")
    print(arr)
    print(f"shape={arr.shape}, ndim={arr.ndim}")
    print(f"解释：{meaning}")


def show_rule(text: str) -> None:
    print(f"规则：{text}")


def demo_vector_matrix_tensor() -> None:
    title("1. 向量、矩阵、张量")

    scalar = np.array(7)
    vector = np.array([10, 20, 30])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    tensor = np.array(
        [
            [[1, 2], [3, 4], [5, 6]],
            [[7, 8], [9, 10], [11, 12]],
        ]
    )

    show_array("scalar", scalar, "一个单独的数，0 维。")
    show_array("vector", vector, "一排数，1 维。")
    show_array("matrix", matrix, "一个表格，2 维。")
    show_array("tensor", tensor, "多个小表格叠在一起，3 维。")


def demo_shape_reading() -> None:
    title("2. 看到 shape 应该怎么读")

    scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    embeddings = np.arange(24).reshape(2, 3, 4)

    show_array("scores", scores, "可以读成 2 个学生，每个学生 3 门成绩。")
    print("读法：shape=(2, 3) -> 2 个对象，每个对象 3 个特征")

    show_array(
        "embeddings",
        embeddings,
        "可以读成 batch=2, seq_len=3, hidden=4。",
    )
    print("读法：shape=(2, 3, 4) -> 2 条样本，每条 3 个位置，每个位置 4 个特征")


def demo_axis() -> None:
    title("3. axis 到底是什么意思")

    scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    show_array("scores", scores, "2 行 3 列的成绩表。")

    by_column = scores.sum(axis=0)
    by_row = scores.sum(axis=1)

    show_array("scores.sum(axis=0)", by_column, "按列相加，所以得到 3 个结果。")
    show_array("scores.sum(axis=1)", by_row, "按行相加，所以得到 2 个结果。")
    show_rule("看 axis 最稳的方法：先算完，再检查哪一维消失了。")


def demo_broadcasting() -> None:
    title("4. broadcasting: 自动对齐，但不是乱补")

    scores = np.array(
        [
            [90, 85, 88],
            [76, 92, 81],
        ]
    )
    bonus_per_subject = np.array([5, 0, 2])
    extra_per_student = np.array([[3], [1]])

    show_array("scores", scores, "shape=(2, 3)，2 个学生 x 3 门课。")
    show_array("bonus_per_subject", bonus_per_subject, "shape=(3,)，每门课分别加分。")
    show_array("extra_per_student", extra_per_student, "shape=(2, 1)，每个学生整体再加分。")

    final_scores = scores + bonus_per_subject
    final_scores_2 = scores + extra_per_student

    show_array(
        "scores + bonus_per_subject",
        final_scores,
        "把同一组科目加分广播到每一行。",
    )
    show_array(
        "scores + extra_per_student",
        final_scores_2,
        "把每个学生自己的加分广播到这一行的每一列。",
    )

    wrong_bonus = np.array([1, 2])
    print("尝试：scores + np.array([1, 2])")
    try:
        print(scores + wrong_bonus)
    except ValueError as exc:
        print(f"报错：{exc}")

    show_rule("从最后一维往前看：相等可以，某一维是 1 也可以，否则不行。")


def demo_elementwise_vs_matmul() -> None:
    title("5. `*` 和 `@` 不是一回事")

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[10, 20], [30, 40]])

    show_array("a", a, "一个 2x2 矩阵。")
    show_array("b", b, "另一个 2x2 矩阵。")
    show_array("a * b", a * b, "逐元素相乘：位置对位置。")
    show_array("a @ b", a @ b, "矩阵乘法：行和列去做组合。")

    show_rule("`*` 看成按位置算，`@` 看成特征变换。")


def demo_matrix_multiplication() -> None:
    title("6. 矩阵乘法为什么会改 shape")

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

    show_array("x", x, "2 条样本，每条样本 3 个特征。")
    show_array("w", w, "把 3 个输入特征映射到 2 个输出特征。")
    y = x @ w
    show_array("x @ w", y, "样本数保留，特征数从 3 变成 2。")
    show_rule("(2, 3) @ (3, 2) -> (2, 2)，中间那个 3 必须对上。")


def demo_model_view() -> None:
    title("7. 放进模型视角里看")

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

    linear_output = x @ w + b

    show_array("x", x, "batch=2, feature=3")
    show_array("w", w, "3 维输入投影到 4 维输出")
    show_array("b", b, "长度 4 的偏置，会广播到每条样本")
    show_array("x @ w + b", linear_output, "这已经是最小版线性层")

    print("模型直觉：")
    print("- x 是输入数据")
    print("- w 决定怎么混合特征")
    print("- b 给每个输出维度一个固定偏移")
    print("- shape 决定这些运算能不能成立")


def mini_quiz() -> None:
    title("8. 快速自测")

    print("题 1：shape=(2, 3, 4) 应该怎么读？")
    print("答案：2 条样本，每条样本 3 个位置，每个位置 4 个特征。")

    print("\n题 2：(2, 3) 和 (3,) 能不能逐元素相加？")
    print("答案：能，(3,) 会被广播到每一行。")

    print("\n题 3：(2, 3) @ (3, 4) 的输出 shape 是多少？")
    print("答案：(2, 4)")

    print("\n题 4：`*` 和 `@` 最大区别是什么？")
    print("答案：`*` 是逐元素算，`@` 是矩阵乘法。")


def summary() -> None:
    title("9. 今天真正要带走的东西")
    print("1. 向量、矩阵、张量都是数组，只是维度不同。")
    print("2. 看数组先看 shape，再问每一维代表谁。")
    print("3. broadcasting 解决逐元素运算时的自动对齐。")
    print("4. 矩阵乘法解决特征变换，shape 会按规则变化。")
    print("5. 这就是后面读模型代码时最基础的张量直觉。")


def main() -> None:
    print("Day 015 补充学习 demo")
    demo_vector_matrix_tensor()
    demo_shape_reading()
    demo_axis()
    demo_broadcasting()
    demo_elementwise_vs_matmul()
    demo_matrix_multiplication()
    demo_model_view()
    mini_quiz()
    summary()


if __name__ == "__main__":
    main()
