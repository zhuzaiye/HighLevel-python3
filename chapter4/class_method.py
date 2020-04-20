# _*_ coding: utf-8 _*_

"""
python 静态方法、类方法以及对象方法
"""


class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # magic method
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    # 类的静态方法，属于类Date的，不是那个实例的对象的，调用是需要通过Date.parse_from_string进行
    # 次式parse_from_string 已经进入Date的定义空间了，不属于那个实例对象，经该方法的命名空间引渡Date中
    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))  # 使用硬编码，不太好

    # 静态方法的硬编码问题是：Date --> NewDate 在调用的时候也要进行修改
    # 为了解决上面问题，使用类方法装饰器，构建类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))  #

    # 实例方法
    def tomorrow(self):
        self.day += 1


"""
if __name__ == '__main__':
    new_day = Date(2020, 4, 19)
    new_day.tomorrow()  # --> tomorrow(new_day) 调用转换
    print(new_day)

    # 静态方法的一个场景: 传递一个字符串惊奇按照某种格式转换
    # 一下部分可以转到类中使用静态方法实现
    date_str = "2020-04-19"
    year, month, day = tuple(date_str.split("-"))
    print(year, month, day)
    day = Date(int(year), int(month), int(day))
    print(day)  # 2020/4/19

    # 用 staticmethod 完成初始化
    # 以上的转换也就成为一下带用方式
    new_day = Date.parse_from_string(date_str)
    print(new_day)  # 2020/4/19
"""
