# Day 027 补充讲义：为什么 next-token prediction 用交叉熵

## 先说结论

今天你要把前面的东西串起来：

> next-token prediction 本质上是一个大规模分类问题，所以特别适合用交叉熵

---

## next-token prediction 是什么

给你一句话的前半段，比如：

```text
I like eating
```

模型要预测下一个 token 是什么。

这不是“随便猜一猜”，而是：

> 从词表里选一个最合适的 token

所以它其实是分类。

---

## 为什么说它是分类问题

因为词表里每个 token 都可以看成一个类别。

模型输出的是对整个词表的打分：

- token 1 一个分
- token 2 一个分
- token 3 一个分
- ...

然后 softmax 变成概率。

最后交叉熵拿它和正确 token 比较。

---

## 为什么不用只看对错

因为“对/错”太粗了。

模型需要的是连续的反馈：

- 这次离正确答案有多远
- 正确 token 的概率是不是太低了

交叉熵正好能给这种反馈。

---

## 你可以把它想成

> 先对词表所有 token 打分，再把正确 token 的概率尽量抬高

这就是训练语言模型最常见的核心逻辑。

---

## 最小 demo

```python
import numpy as np

logits = np.array([0.2, 1.5, -0.3, 0.7, 2.1])
probs = np.exp(logits - np.max(logits))
probs = probs / probs.sum()

print(np.argmax(probs))
print(probs)
```

你要自己先问：

- 词表里谁概率最大？
- 正确 token 是哪一个？
- 如果正确 token 概率很低，会发生什么？

---

## 常见误区

### 误区 1：next-token prediction 不是分类

不对。它就是分类，只是类别很多。

### 误区 2：交叉熵只适合图片分类

不对。语言模型也非常常用。

### 误区 3：输出一个 token 就完事了

不对。训练是对很多位置重复做这个过程。

---

## 你什么时候该问问题

你只要分不清这些，就该问：

- “为什么 next-token prediction 是分类？”
- “词表里的每个 token 都算一个类吗？”
- “为什么要用交叉熵而不是准确率？”

---

## 今天的自测题

1. next-token prediction 为什么是分类问题？
2. 为什么词表里的每个 token 都能看成一个类别？
3. 为什么交叉熵很适合这个任务？
