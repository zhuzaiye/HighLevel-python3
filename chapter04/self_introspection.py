# _*_ coding: utf-8 _*_

"""
self-introspection 自省
通过一定的机制查询对象内部的结构
"""


class Person:
    """
    person
    """
    name = "person"


class Student(Person):
    def __init__(self, my_name):
        self.my_name = my_name


if __name__ == '__main__':
    stu = Student("joe")
    # 通过字典__dict__ 进行查询实例对象的属性
    print(stu.__dict__)  # {'name': 'joe'}
    print(stu.name)  # person 说明父类的类属性是有一定限制，如果字类也同有此属性，将会覆盖父类属性
    print(dir(stu))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ...同样能够输出类属性
    # 说明也可以临时进行键值对的类属性添加
    stu.__dict__["addr"] = "Heaven"
    print(stu.addr)  # Heaven
