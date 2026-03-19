from __future__ import annotations

"""
Day 009 - typing 与函数签名

这个文件按“先核心、后扩展”的顺序放了 7 个例子：
1. 基础函数注解
2. 常见容器类型
3. Union / Optional
4. Any vs object
5. Callable
6. 类型别名
7. TypedDict

说明：
- 这个文件可以在本地 Python 3.9.6 运行。
- 我们也会在案例里展示较新的写法。
- 例如 `int | None` / `int | str` 是 Python 3.10+ 更常见的写法。
- `type Alias = ...` 是 Python 3.12+ 的新语法，这里会放在注释里说明。

继续学习时，又补了 4 个工程基础例子：
8. pathlib
9. json
10. argparse
11. logging
"""

import argparse
import json
import logging
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from collections.abc import Callable
from typing import Any, TypedDict


def show(title: str) -> None:
    print(f"\n=== {title} ===")


# 1. 基础函数注解
def greet_user(name: str, score: int) -> str:
    return f"Hello, {name}. Your score is {score}."


# 2. 常见容器类型
def top_student(scores: dict[str, int]) -> tuple[str, int]:
    best_name = max(scores, key=scores.get)
    return best_name, scores[best_name]


# 3. Union / Optional
# 新写法：Python 3.10+ 常见写法
def parse_retry_count(raw: str) -> int | None:
    raw = raw.strip()
    if raw.isdigit():
        return int(raw)
    return None


def normalize_user_id(value: int | str) -> str:
    return str(value)


# 老写法（3.9 时代常见）：
# from typing import Optional, Union
# def parse_retry_count(raw: str) -> Optional[int]: ...
# def normalize_user_id(value: Union[int, str]) -> str: ...


# 4. Any vs object
def risky_uppercase(value: Any) -> str:
    # Any 的意思更接近“类型检查器先别拦我”
    return value.upper()


def safe_uppercase(value: object) -> str:
    # object 更接近“先承认我不知道具体类型，但使用前必须先判断”
    if isinstance(value, str):
        return value.upper()
    raise TypeError("safe_uppercase only accepts str after narrowing")


# 5. Callable
def apply_formatter(name: str, formatter: Callable[[str], str]) -> str:
    return formatter(name)


def excited(text: str) -> str:
    return text.upper() + "!"


def bracketed(text: str) -> str:
    return f"[{text}]"


# 6. 类型别名
# 3.9 可用写法：
ScoreBoard = dict[str, int]

# 3.12+ 新语法：
# type ScoreBoard = dict[str, int]


def average_score(scores: ScoreBoard) -> float:
    return sum(scores.values()) / len(scores)


# 7. TypedDict
class UserProfile(TypedDict):
    name: str
    age: int
    is_admin: bool


def describe_user(profile: UserProfile) -> str:
    role = "admin" if profile.get('is_admin') else "member"
    return f'{profile["name"]} is {profile["age"]} years old ({role})'


def demo_1_basic_annotations() -> None:
    show("1. 基础函数注解")
    result = greet_user("Alice", 95)
    print("函数签名:", "greet_user(name: str, score: int) -> str")
    print("运行结果:", result)
    print("你要看懂的是：参数类型 + 返回类型 = 这个函数的接口")


def demo_2_containers() -> None:
    show("2. 常见容器类型")
    scores = {"Alice": 95, "Bob": 88, "Carol": 91}
    winner = top_student(scores)
    print("输入数据:", scores)
    print("输出结果:", winner)
    print("你要看懂的是：dict[str, int] 表示“键是 str，值是 int”")


def demo_3_union_optional() -> None:
    show("3. Union / Optional")
    print("新写法: int | None, int | str")
    print("parse_retry_count('3') ->", parse_retry_count("3"))
    print("parse_retry_count('oops') ->", parse_retry_count("oops"))
    print("normalize_user_id(42) ->", normalize_user_id(42))
    print("normalize_user_id('u-7') ->", normalize_user_id("u-7"))
    print("你要看懂的是：一个值可能有多种合法类型，或者可能是 None")


def demo_4_any_vs_object() -> None:
    show("4. Any vs object")
    print("risky_uppercase('hello') ->", risky_uppercase("hello"))
    try:
        print("risky_uppercase(123) ->", risky_uppercase(123))
    except Exception as exc:
        print("risky_uppercase(123) 运行报错 ->", repr(exc))

    print("safe_uppercase('world') ->", safe_uppercase("world"))
    try:
        print("safe_uppercase(123) ->", safe_uppercase(123))
    except Exception as exc:
        print("safe_uppercase(123) 主动拦截 ->", repr(exc))

    print("你要看懂的是：Any 更宽松，object 更安全，但需要先缩小类型范围")


def demo_5_callable() -> None:
    show("5. Callable")
    print("apply_formatter('alice', excited) ->", apply_formatter("alice", excited))
    print(
        "apply_formatter('alice', bracketed) ->",
        apply_formatter("alice", bracketed),
    )
    print("你要看懂的是：Callable[[str], str] 表示“收一个 str，返回一个 str 的函数”")


def demo_6_type_alias() -> None:
    show("6. 类型别名")
    scores: ScoreBoard = {"Alice": 95, "Bob": 88, "Carol": 91}
    print("类型别名名:", "ScoreBoard = dict[str, int]")
    print("平均分:", average_score(scores))
    print("你要看懂的是：类型别名主要是为了让复杂类型更好读，不是创建新运行时类型")


def demo_7_typed_dict() -> None:
    show("7. TypedDict")
    user: UserProfile = {"name": "Alice", "age": 18, "is_admin": False}
    print("输入数据:", user)
    print("输出结果:", describe_user(user))
    print("你要看懂的是：TypedDict 适合描述 JSON / 配置 / 接口返回这种固定键结构")


def demo_8_pathlib() -> None:
    show("8. pathlib")
    with TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        data_dir = base / "data"
        config_path = base / "config.json"

        data_dir.mkdir()
        config_path.write_text('{"env": "dev"}', encoding="utf-8")
        sample_path = data_dir / "sample.txt"
        sample_path.write_text("hello pathlib", encoding="utf-8")

        print("base:", base)
        print("路径拼接:", sample_path)
        print("读取文本:", sample_path.read_text(encoding="utf-8"))
        print("目录内容:", sorted(p.name for p in base.iterdir()))
        print("glob('**/*.txt'):", [p.name for p in base.glob("**/*.txt")])
        print("你要看懂的是：Path 用对象方式表达路径，`/` 用来拼接，read_text/write_text 很常用")


def demo_9_json() -> None:
    show("9. json")
    payload = {
        "model": "tiny-transformer",
        "epochs": 3,
        "tags": ["demo", "week02"],
        "use_gpu": False,
    }
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    decoded = json.loads(encoded)

    print("Python dict -> JSON 字符串:")
    print(encoded)
    print("JSON 字符串 -> Python dict:", decoded)
    print("你要看懂的是：dumps / loads 处理字符串，dump / load 处理文件")


def build_train_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="train_demo.py",
        description="Train a tiny model demo",
    )
    parser.add_argument("data_path", help="path to input json file")
    parser.add_argument("--epochs", type=int, default=3, help="number of epochs")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose output",
    )
    return parser


def demo_10_argparse() -> None:
    show("10. argparse")
    parser = build_train_parser()
    args = parser.parse_args(["data/train.json", "--epochs", "5", "--verbose"])

    print("模拟命令行参数:", ["data/train.json", "--epochs", "5", "--verbose"])
    print("parse_args 结果:", args)
    print("生成的 help 文本:")
    print(parser.format_help().strip())
    print("你要看懂的是：ArgumentParser + add_argument + parse_args 构成命令行接口")


def demo_11_logging() -> None:
    show("11. logging")
    buffer = StringIO()
    logging.basicConfig(
        stream=buffer,
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
        force=True,
    )

    logger = logging.getLogger("day009.demo")
    logger.info("start pipeline")
    logger.warning("config file is missing optional field 'seed'")

    try:
        raise ValueError("bad input shape")
    except ValueError:
        logger.exception("pipeline failed")

    print("日志输出:")
    print(buffer.getvalue().strip())
    print("你要看懂的是：basicConfig 负责快速配置，getLogger(name) 负责按模块/名字记录日志")


def show_quiz() -> None:
    show("3 个判断题")
    print("1. type hint 会在 Python 运行时自动阻止错误类型传入。")
    print("   答案：错。默认主要给类型检查器、IDE、linter 用。")
    print("2. dict[str, int] 的意思是字典键是 str，值是 int。")
    print("   答案：对。")
    print("3. TypedDict 会在运行时把 dict 变成一个全新的特殊对象。")
    print("   答案：错。运行时它仍然只是普通 dict。")


def main() -> None:
    demo_1_basic_annotations()
    demo_2_containers()
    demo_3_union_optional()
    demo_4_any_vs_object()
    demo_5_callable()
    demo_6_type_alias()
    demo_7_typed_dict()
    demo_8_pathlib()
    demo_9_json()
    demo_10_argparse()
    demo_11_logging()
    show_quiz()


if __name__ == "__main__":
    main()
