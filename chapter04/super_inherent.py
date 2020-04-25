# _*_ coding: utf-8 _*_

"""
super
1. 重写了B的构造函数，为什么还要去调用super?
2. super到此执行顺序是怎样的?

多继承 ？？？？
django rest framework 的mixin
1. Mixin类的功能单一，一个类只做一件事
2. 不和基类关联，可以和任何基类组合，尽可能采用组合编码，而不仅多层继承
3. 在Mixin的类中不要私用super
"""


class A:
    def __init__(self, name):
        self.name = name
        print(self.name)
        print("A")


class B(A):
    def __init__(self, name, age):
        print("B")
        self.age = age
        # super可以直接使用父类的属性方法，实现父类代码逻辑在本子类中能够继续使用。
        super().__init__(name=name)


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


if __name__ == '__main__':
    b = B("joe", 21)  # B 如何能加载A的初始化
    c = B("jinLan", 26)  # 输出结果 B jinLan 使用super().__init__(name=name) 就能够使用父类的该属性的方法
    d = D()  # super按照mro的方法调用，顺序 D-B-C-A
