# _*_ coding: utf-8 _*_

"""
__new__ and __init___

-- new 在init之前，即在对象生成之前，控制对象的生成过程
-- init 用于来完善对象
-- new 方法不返回对象，则不会带哦用init函数
"""


class User:
    def __new__(cls, *args, **kwargs):
        # 这里控制生成“类”的逻辑，就是去控制User的生成的属性
        print("in new")
        return super().__new__(cls)

    def __init__(self, name):
        # 这里是控制User实例生成的逻辑，就是控制main中user的生成逻辑
        pass


if __name__ == '__main__':
    user = User(name="joe")  # 在init中没有name是会报错TypeError: __init__() got an unexpected keyword argument 'name'，
    # 也就是说实例化的参数只能存活于init中的预先定义
