from __future__ import annotations

"""
Day 010 - 异常处理 (Exceptions)

这个文件按"先核心、后扩展"的顺序放了 7 个例子：
1. 基本 try-except
2. 多个异常类型
3. else 子句
4. finally 子句
5. raise 抛出异常
6. 自定义异常
7. 异常链

说明：
- 异常是 Python 错误处理的核心机制
- 掌握 try-except 是最基础的要求
- 理解 else/finally 的执行时机很重要
"""

from typing import Any


def show(title: str) -> None:
    print(f"\n=== {title} ===")


# ============================================================
# 1. 基本 try-except
# ============================================================

def safe_divide(a: int, b: int) -> float | None:
    """安全除法，避免除零错误"""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"  捕获异常: 不能除以零 ({a} / {b})")
        return None


def safe_convert(text: str) -> int | None:
    """安全转换为整数"""
    try:
        return int(text)
    except ValueError:
        print(f"  捕获异常: '{text}' 不是有效的整数")
        return None


# ============================================================
# 2. 多个异常类型
# ============================================================

def safe_list_get(items: list[Any], index: int) -> Any | None:
    """安全获取列表元素"""
    try:
        return items[index]
    except (IndexError, TypeError):
        # 同时捕获索引越界和类型错误（比如 items 不是列表）
        print(f"  捕获异常: 无法获取索引 {index}")
        return None


def safe_divide_any(a: Any, b: Any) -> float | None:
    """处理多种可能的异常"""
    try:
        return float(a) / float(b)
    except (ValueError, TypeError) as e:
        print(f"  捕获异常: 类型转换失败 - {e}")
        return None
    except ZeroDivisionError:
        print(f"  捕获异常: 除零错误")
        return None


# ============================================================
# 3. else 子句
# ============================================================

def divide_with_else(a: int, b: int) -> float | None:
    """
    else 子句在没有异常时执行
    好处：让 try 块更精简，只包含可能出错的代码
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  捕获异常: 除零错误")
        return None
    else:
        # 没有异常时执行到这里
        print(f"  除法成功: {a} / {b} = {result}")
        return result


def read_file_safe(filepath: str) -> str | None:
    """读取文件，使用 else 处理成功情况"""
    try:
        f = open(filepath, encoding="utf-8")
    except FileNotFoundError:
        print(f"  捕获异常: 文件不存在 - {filepath}")
        return None
    else:
        content = f.read()
        f.close()
        print(f"  文件读取成功，共 {len(content)} 字符")
        return content


# ============================================================
# 4. finally 子句
# ============================================================

def divide_with_finally(a: int, b: int) -> float | None:
    """
    finally 无论是否异常都会执行
    常用于资源清理（关闭文件、释放锁等）
    """
    print(f"  开始计算 {a} / {b}")
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"  捕获异常: 除零错误")
        return None
    finally:
        # 无论成功还是异常，都会执行
        print(f"  finally: 计算结束（无论成功失败）")


def file_operation_demo(filepath: str) -> None:
    """演示 finally 在文件操作中的使用"""
    f = None
    try:
        f = open(filepath, encoding="utf-8")
        content = f.read()
        print(f"  文件内容: {content[:50]}...")
    except FileNotFoundError:
        print(f"  捕获异常: 文件不存在")
    finally:
        print(f"  finally: 清理资源")
        if f:
            f.close()
            print(f"  文件已关闭")


# ============================================================
# 5. raise 抛出异常
# ============================================================

def set_age(age: int) -> None:
    """主动抛出异常"""
    if age < 0:
        raise ValueError(f"年龄不能为负数: {age}")
    if age > 150:
        raise ValueError(f"年龄不合理: {age}")
    print(f"  年龄设置成功: {age}")


def reraise_demo() -> None:
    """演示重新抛出异常"""
    try:
        raise RuntimeError("原始错误")
    except RuntimeError as e:
        print(f"  捕获到异常: {e}")
        raise  # 直接重新抛出，保留原始堆栈


# ============================================================
# 6. 自定义异常
# ============================================================

class InsufficientBalanceError(Exception):
    """余额不足异常"""

    def __init__(self, balance: float, required: float) -> None:
        self.balance = balance
        self.required = required
        super().__init__(f"余额不足: 当前 {balance}, 需要 {required}")


class InvalidConfigError(Exception):
    """配置无效异常"""

    def __init__(self, key: str, value: Any, reason: str) -> None:
        self.key = key
        self.value = value
        self.reason = reason
        super().__init__(f"配置无效 [{key}={value}]: {reason}")


def withdraw(balance: float, amount: float) -> float:
    """取款示例，使用自定义异常"""
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount


def validate_config(config: dict[str, Any]) -> None:
    """验证配置，使用自定义异常"""
    if "port" in config:
        port = config["port"]
        if not isinstance(port, int):
            raise InvalidConfigError("port", port, "必须是整数")
        if not (1 <= port <= 65535):
            raise InvalidConfigError("port", port, "必须在 1-65535 范围内")


# ============================================================
# 7. 异常链 (raise ... from)
# ============================================================

def load_config_from_file(filepath: str) -> dict[str, Any]:
    """
    异常链：将底层异常包装成更高级的异常
    使用 raise ... from 保留原始异常信息
    """
    try:
        f = open(filepath, encoding="utf-8")
    except FileNotFoundError as e:
        raise RuntimeError(f"配置文件加载失败: {filepath}") from e
    else:
        import json

        content = f.read()
        f.close()
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"配置文件格式错误: {filepath}") from e


# ============================================================
# Demo 函数
# ============================================================


def demo_1_basic_try_except() -> None:
    show("1. 基本 try-except")
    print("safe_divide(10, 2) ->", safe_divide(10, 2))
    print("safe_divide(10, 0) ->", safe_divide(10, 0))
    print()
    print("safe_convert('42') ->", safe_convert("42"))
    print("safe_convert('hello') ->", safe_convert("hello"))
    print("你要看懂的是：try 块放可能出错的代码，except 块处理异常")


def demo_2_multiple_exceptions() -> None:
    show("2. 多个异常类型")
    print("safe_list_get([1, 2, 3], 1) ->", safe_list_get([1, 2, 3], 1))
    print("safe_list_get([1, 2, 3], 10) ->", safe_list_get([1, 2, 3], 10))
    print()
    print("safe_divide_any('10', '2') ->", safe_divide_any("10", "2"))
    print("safe_divide_any('10', '0') ->", safe_divide_any("10", "0"))
    print("safe_divide_any('a', 'b') ->", safe_divide_any("a", "b"))
    print("你要看懂的是：可以用元组捕获多种异常，或写多个 except 块")


def demo_3_else_clause() -> None:
    show("3. else 子句")
    divide_with_else(10, 2)
    divide_with_else(10, 0)
    print()
    read_file_safe("不存在的文件.txt")
    print("你要看懂的是：else 在没有异常时执行，让 try 块更精简")


def demo_4_finally_clause() -> None:
    show("4. finally 子句")
    divide_with_finally(10, 2)
    print()
    divide_with_finally(10, 0)
    print("你要看懂的是：finally 无论是否异常都会执行，用于资源清理")


def demo_5_raise() -> None:
    show("5. raise 抛出异常")
    set_age(25)

    try:
        set_age(-5)
    except ValueError as e:
        print(f"  捕获异常: {e}")

    try:
        set_age(200)
    except ValueError as e:
        print(f"  捕获异常: {e}")

    print("你要看懂的是：raise 用于主动抛出异常，常用于参数校验")


def demo_6_custom_exception() -> None:
    show("6. 自定义异常")
    try:
        withdraw(100, 50)
        print("  取款成功，余额: 50")
    except InsufficientBalanceError as e:
        print(f"  捕获异常: {e}")

    try:
        withdraw(100, 150)
    except InsufficientBalanceError as e:
        print(f"  捕获异常: {e}")
        print(f"  当前余额: {e.balance}, 需要: {e.required}")

    print()
    try:
        validate_config({"port": "hello"})
    except InvalidConfigError as e:
        print(f"  捕获异常: {e}")
        print(f"  键: {e.key}, 值: {e.value}, 原因: {e.reason}")

    print("你要看懂的是：自定义异常可以携带更多上下文信息")


def demo_7_exception_chain() -> None:
    show("7. 异常链")
    try:
        load_config_from_file("不存在的配置.json")
    except RuntimeError as e:
        print(f"  捕获高级异常: {e}")
        print(f"  原始异常: {e.__cause__}")

    print("你要看懂的是：raise ... from 保留原始异常，方便调试")


def show_quiz() -> None:
    show("3 个判断题")
    print("1. try 块里只有一行代码出错，整个 try 块都会停止执行。")
    print("   答案：对。一旦出错立即跳到 except。")
    print()
    print("2. else 和 finally 不能同时出现在同一个 try 语句里。")
    print("   答案：错。可以同时使用，else 在无异常时执行，finally 始终执行。")
    print()
    print("3. except Exception 会捕获所有异常。")
    print("   答案：不完全对。它会捕获大部分异常，但 BaseException 的其他子类（如 KeyboardInterrupt）不会被捕获。")


def show_common_exceptions() -> None:
    show("常见异常类型速查")
    exceptions = [
        ("ValueError", "值错误，如 int('abc')"),
        ("TypeError", "类型错误，如 '1' + 1"),
        ("KeyError", "字典键不存在"),
        ("IndexError", "列表索引越界"),
        ("FileNotFoundError", "文件不存在"),
        ("ZeroDivisionError", "除以零"),
        ("AttributeError", "对象没有该属性"),
        ("NameError", "变量未定义"),
        ("RuntimeError", "通用运行时错误"),
        ("StopIteration", "迭代器耗尽"),
    ]
    for name, desc in exceptions:
        print(f"  {name:25} - {desc}")


def main() -> None:
    demo_1_basic_try_except()
    demo_2_multiple_exceptions()
    demo_3_else_clause()
    demo_4_finally_clause()
    demo_5_raise()
    demo_6_custom_exception()
    demo_7_exception_chain()
    show_common_exceptions()
    show_quiz()


if __name__ == "__main__":
    main()
