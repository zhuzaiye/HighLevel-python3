"""
1、类变量和实例变量的认识
2、类变量和实例变量的区别
"""


class A:
    # 类变量, 永远不可能通过实例进行修改，只能通过类自己进行修改
    # aa是所有实例共享的
    aa = 1

    def __init__(self, x, y):
        self.x = x  # 实例变量
        self.y = y


if __name__ == '__main__':
    a = A(2, 3)  # 实例化
    # 对A类进行类变量修改
    A.aa = 11
    # 这里其实不是修改A.aa这个类变量，而是重新创建一个和x,y一样的aa实例变量
    a.aa = 100
    print(a.x, a.y, a.aa)  # 2 3 100
    print(A.aa)  # 11

    # 重新实例化b
    b = A(4, 5)
    print(b.aa)  # 11
