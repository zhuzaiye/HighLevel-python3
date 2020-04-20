# _*_ coding: utf-8 _*_

"""
通过二分查找的处理已排序的可变序列，用来维持一个始终有序的数据序列。
----------- Bisection algorithms. -------------------------------
insort_right(a, x, lo=0, hi=None) -->
    Insert item x in list a, and keep it sorted assuming a is sorted.
    If x is already in a, insert it to the right of the rightmost x.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

bisect_right(a, x, lo=0, hi=None) -->
    Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

insort_left(a, x, lo=0, hi=None) --> bisect_left(a, x, lo=0, hi=None)
    Insert item x in list a, and keep it sorted assuming a is sorted.
    If x is already in a, insert it to the left of the leftmost x.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
"""

import bisect

if __name__ == '__main__':
    insert_int = []
    bisect.insort(insert_int, 6)
    bisect.insort(insert_int, 1)
    bisect.insort(insert_int, 5)
    bisect.insort(insert_int, 3)
    bisect.insort(insert_int, 7)
    bisect.insort(insert_int, 2)
    bisect.insort(insert_int, 4)

    print(insert_int)  # [1, 2, 3, 4, 5, 6, 7]
