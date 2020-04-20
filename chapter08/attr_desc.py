# _*_ coding: utf-8 _*_

import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("the filed is not Integral")
        self.value = value

    def __delete__(self, instance):
        pass


class User:
    age = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.age)  # 30
    user.age = "not int"
    print(user.age)  # ValueError: the filed is not Integral
