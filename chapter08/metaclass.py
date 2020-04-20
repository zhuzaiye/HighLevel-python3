# _*_ coding: utf-8 _*_

"""
meta class 元类编程

元类是创建类的类， 比如对象<- class <- type
也就是说利用type来创建一个类，这个类可以继续实例化使用
抓换一种思想，一切皆对象，于是说类对于type来说也是其一个实例化对象
---------------
type
    def __init__(cls, what, bases=None, dict=None): # known special case of type.__init__

        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        # (copied from class doc)

        pass
type 可以创建类
"""


# 动态创建类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


# type动态创建类
# User = type("User", (), {"name": "user"})

def say(self):
    return "i am user"
    # return self.ane


class BaseClass:
    def answer(self):
        return "I am base class"


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)  # 使用type的方法和参数


class User(metaclass=MetaClass):
    """
        python中创建类的实例化过程，会首先寻找metaclass， 通过metaclass去创建user类
        然后再去创建类独享，实例化
        """

    def __init__(self):
        pass

    def __str__(self):
        return "创建类的元类剥离"


if __name__ == '__main__':
    # MyClass = create_class("user")
    # obj = MyClass()
    # print(obj)

    User = type("user", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.name)  # user
    print(my_obj.say())  # i am user
    print(my_obj.answer())  # I am base class
