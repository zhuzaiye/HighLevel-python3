# _*_ coding: utf-8 _*_

"""
contextlib 实现 with 的简单上下文协议
"""
import contextlib


@contextlib.contextmanager  # 将file_open装饰为with上下文协议
def file_open(file_name):
    print("file open")  # --1
    # yield 之前的都是去实现魔术函数 __enter__
    yield {}  # 一定必须有yield 生成器逻辑是为了将“主体逻辑”进行保存
    # yield 之后的都是是新啊魔术函数 __exit__
    print("file end")  # --3


# file_open函数就能使用with函数
with file_open("text.txt") as f:
    # 于此写“主体逻辑”
    print("file processing")  # yield --2

"""
1. 输出结果
    file open  --1
    file processing  --2
    file end  --3
2. @contextmanager decorator.
    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
"""
