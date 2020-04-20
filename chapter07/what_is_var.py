# _*_ coding: utf-8 _*_

"""
python的变量实质上是一个指针指向int, str，类似便利贴
--------------------------------------------
is and ==
"""

if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    # 先生成对象，然后对象指针指向一段内存
    # 类似便利贴一样
    print(id(a), id(b))  # 1749052290952 1749052290952
    print(a is b)  # True
    print(id(a), id(c))  # 2783565313928 2783565277960
    print(a is c)  # False
    print(a == c)  # True
    # -------------------
    # 对于小的不可变变量类型，python的方式是建立一个全局的地址
    d = 1
    e = 1
    print(id(d), id(e))  # 1357144288 1357144288
    print(d is e)  # True

