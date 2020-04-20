# _*_ coding: utf-8 _*_
"""
property的动态属性的装饰器
"""

from datetime import date, datetime


class User:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birth.year

    @property  # 这是一个get的属性
    def age(self):  # 取代上面的get_age对象函数，将函数行为转变为类的一个属性
        return datetime.now().year - self.birth.year

    @age.setter  # 这是一个property的 set属性
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User("joe", date(1992, 2, 5))
    print(user.age)  # 28
    user.age = 30
    print(user._age)  # 30
