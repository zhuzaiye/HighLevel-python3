# _*_ coding: utf-8 _*_

"""
实现一个具有切片功能的对象.
----------------------
1.
2.
3.
4.
5.
"""
import numbers


class Group:
    """
    实现一个可以具有切片、反转等功能的不可变序列的对象。
    """

    def __init__(self, name, company, staffs):
        self.name = name
        self.company = company
        self.staffs = staffs

    # 实现翻转功能 object.reversed()
    def __reversed__(self):
        # 利用list的reverse方法
        self.staffs.reverse()

    # 实现切片功能的抽象方法
    def __getitem__(self, item):
        # return self.staffs[item]  # 返回是一个list
        # 下面切片返回还是group对象，不再是上面的而返回为list
        cls = type(self)
        if isinstance(item, slice):
            return cls(name=self.name, company=self.company, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(name=self.name, company=self.company, staffs=list(self.staffs[item]))

    # object.len()
    def __len__(self):
        return len(self.staffs)

    # 对象可迭代的方法
    def __iter__(self):
        return iter(self.staffs)

    # 实现 in 判断的抽象方法
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


if __name__ == '__main__':
    g = Group(name="JinLan", company="hospital", staffs=["beautiful", "beautiful1", "beautiful2", "beautifu3"])
    rst = g[:2]  # 都是pass 运行至此不会报错的原因就是__getitem__()的存在，注释该魔术函数，将会报错
    print(rst.name, rst.company, rst.staffs)  # JinLan hospital ['beautiful', 'beautiful1']
    length = len(g)
    print(length)  # 4
    if "beautiful" in g:
        print("exist")  # exist
