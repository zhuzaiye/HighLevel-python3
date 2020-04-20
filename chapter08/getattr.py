# _*_ coding: utf-8 _*_

"""
__getattr__ and __getattribute__
---------------------------------

"""

from datetime import date, datetime


class User:
    def __init__(self, name, birth, addr={}):
        self.name = name
        self.birth = birth
        # self._age = 0
        self.addr = addr

    # 添加__getattr__ 当查找不到某个属性，就会返回一份错误，程序不会崩溃
    def __getattr__(self, item):
        # [set codes]
        print("not find attr")
        return self.addr[item]  # 将item作为类的属性

    # 所有属性都会被这个捕获而返回，慎用
    def __getattribute__(self, item):
        return "all attr will return without if the attr is not exist."


if __name__ == '__main__':
    user = User("joe", date(1992, 2, 5), {"key": "beijing"})
    # print(user.age)  # AttributeError: 'User' object has no attribute 'age' --> not find attr
    print(user.key)  # beijing
    print(user.norkey)
