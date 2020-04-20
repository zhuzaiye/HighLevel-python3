# _*_ coding: utf-8 _*_

"""
list这种可变数据类型的传参的问题
"""


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com1 = Company("com1", ["c1", "c2"])
    com1.add("c3")
    com1.remove("c1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("c4")
    print(com2.staffs)  # ['c4']

    print(Company.__init__.__defaults__)  # (['c4'],)

    com3 = Company("com3")
    com3.add("c5")
    print(com2.staffs)  # ['c4', 'c5']
    print(com3.staffs)  # ['c4', 'c5']

    """
    由此可得：
        当list作为参数传递时，注意其可能被指向同一个地址，而导致被其他函数进行修改。
    """

