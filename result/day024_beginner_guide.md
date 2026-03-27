# Day 024 补充讲义：softmax

## 先说结论

今天你只需要记住一句话：

> softmax 会把一组原始分数变成概率分布

---

## softmax 在做什么

假设 logits 是：

```python
[2.0, 1.0, 0.1]
```

softmax 会把它变成类似这样的概率：

```python
[0.66, 0.24, 0.10]
```

它做到了两件事：

- 每个数都变成正数
- 总和变成 1

---

## 为什么要用 softmax

因为模型先输出的是分数，不是概率。

softmax 的作用是：

> 把“谁更强”变成“每个答案有多大概率”

---

## softmax 的直觉

分高的答案会拿到更大的概率。

分低的答案会拿到更小的概率。

但它不会把“排序”完全打乱。

如果原来第 1 名最高，softmax 后通常还是第 1 名最高。

---

## 一个重要细节

工程上经常会先把 logits 减去最大值。

这是为了避免数值太大。

你可以先把这件事理解成：

> 不是在改答案，只是在让计算更稳

---

## 最小 demo

```python
import numpy as np

logits = np.array([2.0, 1.0, 0.1])
shifted = logits - np.max(logits)
probs = np.exp(shifted) / np.exp(shifted).sum()

print(probs)
print(probs.sum())
```

你先看两件事：

- 输出是不是全正数
- 加起来是不是 1

---

## 常见误区

### 误区 1：softmax 只是“换个写法”

不对。它是在把分数变成概率。

### 误区 2：softmax 会改变最大项是谁

一般不会。

### 误区 3：softmax 前后 shape 会变

通常不会。它更多是改数值，不改 shape。

---

## 你什么时候该问问题

你只要分不清这些情况，就该问：

- “softmax 前后分别是什么？”
- “为什么输出是概率？”
- “为什么要先减最大值？”
- “softmax 是不是会改变谁最大？”

---

## 今天的自测题

1. softmax 的作用是什么？
2. softmax 为什么输出和为 1？
3. 为什么要先减最大值？
