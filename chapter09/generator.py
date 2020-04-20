# _*_ coding: utf-8 _*_

"""
生成器函数。只要函数内存在yield关键子，就是生成器函数
不如说是生成对象器
"""


def gen_func():
    yield 1
    yield 2
    yield 3


"""
生成器：惰性求值，为延迟求值提供可能
"""


def func():
    return 1


if __name__ == '__main__':
    gen = gen_func()  # gen是一个对象， 在python'编译字节码得时候产生对象
    # gen 是一个可迭代对象
    for value in gen:
        print(value)  # 1 2 3
    re = func()  # re 是一个值
    pass
