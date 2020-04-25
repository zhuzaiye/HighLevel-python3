# _*_ coding: utf-8 _*_

"""
python 私有
"""
from high_order_py3.chapter4.class_method import Date
import datetime


class User:
    def __init__(self, birthday):
        # self.birthday = birthday # 这样的变量是公开的
        self.__birthday = birthday  # 私有属性，外部不能访问

    def get_age(self):
        return datetime.datetime.now().year - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1992, 2, 1))
    # print(user.__birthday)  # AttributeError: 'User' object has no attribute '__birthday'
    print(user._User__birthday)  # 能访问到私有属性
    print(user.get_age())
