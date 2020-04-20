# _*_ coding: utf-8 _*_

"""
MRO-->
C3 算法 --python3 多继承 方法属性查询算法
"""


class A:
    # 类也是对象
    name = "A"

    def __init__(self):
        self.name = "obj"


# 实验查看python的C3查询算法
class D:
    pass


class E:
    pass


# 菱形继承结构
# class C(D):
#     pass

class C(E):
    pass


# 菱形继承结构
# class B(C):
#     pass

class B(D):
    pass


class A1(B, C):
    pass


if __name__ == '__main__':
    a = A()
    # a.name 是如何查找的？自下而上的搜查方法，从实例到类
    print(a.name)  # obj

    # 类性查询顺序(<class '__main__.A1'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
    # print(A1.__mro__) # 菱形继承结构

    # (<class '__main__.A1'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>,
    # <class 'object'>)
    print(A1.__mro__)
