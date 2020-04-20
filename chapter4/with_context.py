# _*_ coding: utf-8 _*_

"""
try except finally
"""
"""
try:
    # 引出with的使用原因
    f_open = open("test.txt")
    print("code start")
    raise KeyError
    # f_open.close() # raise以后是达不到，于是需要在except中添加
except KeyError as e:
    print("key error")
    f_open.close()
# else:  # 如果上面有raise else的内容是达不到的
#     print("other")
finally:
    print("finally")
"""


def exe_try():
    try:
        print("code started")
        raise KeyError
        return 1  # --- 1
    except KeyError as e:
        print("key error")
        return 2  # --- 2
    else:
        print("other error")
        return 3  # --- 3
    finally:
        print("finally")
        return 4  # --- 4


# 上下文管理器协议 重要设计的魔法函数是 __enter__ 和 __exit__
class Sample:
    def __enter__(self):
        print("enter")
        # enter 段可以获取资源功能, python解释器自动调用

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        # exit 可以释放资源功能, python解释器自动调用

    def do_something(self):
        print("do something")


# __enter__ 和 __exit__ 自定义类只要有这两个魔术函数，就能实现with上下文协议的使用
with Sample() as sample:
    sample.do_something()

# if __name__ == '__main__':
#     result = exe_try()
#     print(result)  # code started --> key error --> finally --> 4
    """
    return的结果是“4”, 原因：
    1. 在---1步，由于raise 所以不会return
    2. 在---2步， 由于finally有return，所以“2”会被压入栈
    3. 在---3步， 由于try有raise所以该处不会执行
    4. 在---4步， 此时return会把“4”压入栈，于是在调用返回时就把栈顶的“4”返回
    5. 如果想吧“2”输出，只需要把finally的return注释，这样栈顶的数字是“2”
    """
