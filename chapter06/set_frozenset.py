# _*_ coding: utf-8 _*_

"""
set 无序不重复序列
"""

if __name__ == '__main__':
    s = set("abcdee")
    print(s)  # {'a', 'e', 'c', 'd', 'b'}
    s.add("e")
    s.update({"3", "4"})

    fs = frozenset("abcde")
    # fs.add() 不能
    print(fs)  # frozenset({'c', 'd', 'a', 'e', 'b'})
