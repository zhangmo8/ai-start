from __future__ import annotations

"""
Week 04 学习 demo：概率、Softmax、交叉熵与梯度直觉

运行：
    python3 test/week04_learning_pack.py
"""

import numpy as np


np.set_printoptions(precision=4, suppress=True)


def title(text: str) -> None:
    print(f"\n=== {text} ===")


def show_vec(name: str, vec: np.ndarray, meaning: str) -> None:
    print(f"{name}: {vec}")
    print(f"shape={vec.shape}")
    print(f"解释：{meaning}")


def softmax(logits: np.ndarray) -> np.ndarray:
    shifted = logits - np.max(logits)
    exp = np.exp(shifted)
    return exp / exp.sum()


def cross_entropy(probs: np.ndarray, target_index: int) -> float:
    return float(-np.log(probs[target_index] + 1e-12))


def demo_logits_vs_probability() -> None:
    title("1. logits 不是概率")

    logits = np.array([2.0, 1.0, 0.1])
    show_vec("logits", logits, "模型给三个候选答案打的原始分数。")
    print("它们可以是任意实数，不需要加起来等于 1。")
    print(f"最大分数的位置是：{np.argmax(logits)}")

    shifted = logits + 10
    show_vec("logits + 10", shifted, "把所有分数一起平移。")
    print(f"平移后最大分数的位置还是：{np.argmax(shifted)}")


def demo_softmax() -> None:
    title("2. softmax: 把分数变成概率")

    logits = np.array([2.0, 1.0, 0.1])
    probs = softmax(logits)

    show_vec("logits", logits, "原始分数。")
    show_vec("softmax(logits)", probs, "概率分布，每个值都在 0 到 1 之间。")
    print(f"概率和 = {probs.sum():.4f}")
    print(f"最大概率的位置 = {np.argmax(probs)}")

    print("softmax 的直觉：分高的更容易拿到更大的概率。")


def demo_softmax_shift_invariance() -> None:
    title("3. softmax 不怕整体平移")

    logits = np.array([2.0, 1.0, 0.1])
    shifted = logits + 100.0

    probs_1 = softmax(logits)
    probs_2 = softmax(shifted)

    show_vec("softmax(logits)", probs_1, "原始结果。")
    show_vec("softmax(logits + 100)", probs_2, "整体平移后，概率几乎不变。")
    print("这说明 softmax 关心的是相对大小，不是绝对数值。")


def demo_cross_entropy() -> None:
    title("4. 交叉熵: 正确答案概率越低，惩罚越大")

    target = 0
    good_probs = np.array([0.75, 0.20, 0.05])
    bad_probs = np.array([0.10, 0.70, 0.20])

    show_vec("good_probs", good_probs, "模型把较高概率给了正确答案。")
    show_vec("bad_probs", bad_probs, "模型把很低概率给了正确答案。")

    good_loss = cross_entropy(good_probs, target)
    bad_loss = cross_entropy(bad_probs, target)

    print(f"good_loss = {good_loss:.4f}")
    print(f"bad_loss  = {bad_loss:.4f}")
    print("正确答案概率越小，loss 越大。")


def ce_gradient_from_logits(logits: np.ndarray, target_index: int) -> tuple[np.ndarray, float, np.ndarray]:
    probs = softmax(logits)
    loss = cross_entropy(probs, target_index)
    grad = probs.copy()
    grad[target_index] -= 1.0
    return probs, loss, grad


def demo_gradient_descent_on_loss() -> None:
    title("5. 梯度下降先看一个最简单的例子")

    w = 0.0
    lr = 0.2

    print("我们先看一个最简单的函数：f(w) = (w - 3)^2")
    for step in range(5):
        loss = (w - 3) ** 2
        grad = 2 * (w - 3)
        print(f"step {step}: w={w:.4f}, loss={loss:.4f}, grad={grad:.4f}")
        w = w - lr * grad

    print("你可以把它理解成：梯度告诉你坡往哪边斜，更新就往反方向走。")


def demo_softmax_cross_entropy_update() -> None:
    title("6. softmax + cross entropy 的训练信号")

    logits = np.array([1.0, 0.5, -0.5])
    target = 0
    lr = 0.5

    print("目标：让第 0 类的概率越来越大。")
    for step in range(5):
        probs, loss, grad = ce_gradient_from_logits(logits, target)
        print(f"step {step}:")
        print(f"  logits = {logits}")
        print(f"  probs  = {probs}")
        print(f"  loss   = {loss:.4f}")
        print(f"  grad   = {grad}")
        logits = logits - lr * grad

    print("你会看到：正确类别的概率在上升，loss 在下降。")


def demo_one_hot_view() -> None:
    title("7. one-hot 和交叉熵")

    probs = np.array([0.66, 0.24, 0.10])
    target = 0
    one_hot = np.array([1.0, 0.0, 0.0])

    show_vec("probs", probs, "模型预测的概率分布。")
    show_vec("one_hot", one_hot, "正确答案的表示方式。")

    loss = -np.sum(one_hot * np.log(probs + 1e-12))
    print(f"交叉熵 loss = {loss:.4f}")
    print("one-hot 的作用：告诉模型谁才是正确类别。")


def demo_next_token_view() -> None:
    title("8. next-token prediction 为什么像分类")

    vocab_size = 5
    logits = np.array([0.2, 1.5, -0.3, 0.7, 2.1])
    target_token = 4

    show_vec("vocab logits", logits, f"词表里 {vocab_size} 个 token 的打分。")
    probs = softmax(logits)
    show_vec("vocab probs", probs, "每个 token 的概率。")
    print(f"预测的 token = {np.argmax(probs)}")
    print(f"真实的 token = {target_token}")
    print(f"真实 token 的交叉熵 = {cross_entropy(probs, target_token):.4f}")
    print("所以 next-token prediction 本质上就是一个大规模多分类问题。")


def summary() -> None:
    title("9. 你今天真正要带走的东西")
    print("1. logits 是原始分数，不是概率。")
    print("2. softmax 把分数变成概率分布。")
    print("3. cross entropy 关注正确答案概率有多大。")
    print("4. 梯度下降会沿着让 loss 变小的方向更新参数。")
    print("5. next-token prediction 本质上是对词表做分类。")


def main() -> None:
    print("Week 04 学习 demo")
    demo_logits_vs_probability()
    demo_softmax()
    demo_softmax_shift_invariance()
    demo_cross_entropy()
    demo_gradient_descent_on_loss()
    demo_softmax_cross_entropy_update()
    demo_one_hot_view()
    demo_next_token_view()
    summary()


if __name__ == "__main__":
    main()
