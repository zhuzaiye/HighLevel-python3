# _*_ coding: utf-8 _*_

"""
1.首先观看python函数是如何一步步工作的。
    python.exe是一个叫做PyEval_EvalFrameEx（c函数）去执行函数
    首先会创建一个栈帧。
    于此，一切皆对象就体现了，上面产生的栈帧也是一个对象， 对函数进行字节码编译，也会产生一个字节码对象
2.下面的foo调用函数bar，还会创建一个栈帧，所有栈帧都是分配在堆上的，这就决定栈帧可以独立于调用者存在
3. heap memory 生成器的栈帧对现象是建立在堆上的，结构如下
    在程序退出后，堆上仍能产看生成器的栈帧对象，于是这就为协程的实现奠定理论基础。
    PyGenObject--
               -- gi_frame -->
                           -->PyFrameObject --
                                            -- f_lasti
                                            -- f_locals
               -- fi_code -->
                          --> PyCodeObject --
                                           --gen_fn's bytecode
"""

import dis


def foo():
    bar()


def bar():
    pass


def gen_func():
    yield 1
    name = "python"
    yield 2
    age = 30
    return "ok"


if __name__ == '__main__':
    # print(dis.dis(foo))
    """
     14       0 LOAD_GLOBAL              0 (bar)  首先加载全局 bar
              2 CALL_FUNCTION            0        其次调用函数
              4 POP_TOP                           然后是栈帧对象
              6 LOAD_CONST               0 (None) 接着是加载常量，没有默认None
              8 RETURN_VALUE                      最后返回值， 没有就是None
     None
    """

    gen = gen_func()
    print(dis.dis(gen))
    """
     23           0 LOAD_CONST               1 (1)
                  2 YIELD_VALUE
                  4 POP_TOP

     24           6 LOAD_CONST               2 ('python')
                  8 STORE_FAST               0 (name)
    
     25          10 LOAD_CONST               3 (2)
                 12 YIELD_VALUE
                 14 POP_TOP
    
     26          16 LOAD_CONST               4 (30)
                 18 STORE_FAST               1 (age)
    
     27          20 LOAD_CONST               5 ('ok')
                 22 RETURN_VALUE
    None
    """

    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)

