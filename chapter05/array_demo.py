# _*_ coding: utf-8 _*_

"""
array and deque
----------
array 只能存储固定类型数据
"""

import array

if __name__ == '__main__':
    my_array = array.array("i")
    my_array.append(1)
    print(my_array)