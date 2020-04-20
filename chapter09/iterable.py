# _*_ coding: utf-8 _*_

"""
1.什么迭代协议？
2.迭代器是什么？
    迭代器是访问集合内元素的元素的一种方式，一般用来遍历数据。
3.迭代器是不能返回的，得带起提供了一种惰性方式的数据
4. __iter__ 是说明可迭代， __next__才是迭代器的本质
"""

from collections.abc import Iterable, Iterator


class MyIterator(Iterator):
    """
    迭代器
    """
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    # def __iter__(self):
    #     pass

    def __next__(self):
        # 真正的返回迭代值得逻辑
        # 迭代器不支持切片，只能迭代
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class Company:
    """
    可迭代对象
    """
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)
    #
    # def __getitem__(self, item):
    #     return self.employee[item]


if __name__ == '__main__':
    # a = [1, 2]
    # iter_rator = iter(a)
    # print(isinstance(a, Iterable))  # True
    # print(isinstance(a, Iterator))  # False
    # print(isinstance(iter_rator, Iterator))  # True
    company = Company(["tom", "bob", "jane"])
    my_itor = iter(company)
    #
    # while True:
    #     try:
    #         print(next(my_itor))
    #     except StopIteration:
    #         pass
    for item in my_itor:
        print(item)
