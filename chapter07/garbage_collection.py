# _*_ coding: utf-8 _*_

"""
cpython
-- 垃圾回收方法  引用计数
-- python解释器回收某些对象释放一些资源，在object中加入 __del__
    class A:
        def __del__(self):
            pass
"""

if __name__ == '__main__':
    a = 1
    b = a
    # 将指向1的引用a删除，计数减1
    del a
    print(a)  # NameError: name 'a' is not defined
    print(b)  # 1
