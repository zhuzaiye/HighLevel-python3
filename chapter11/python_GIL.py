# _*_ coding: utf-8 _*_

"""
GIL: Global interpreter lock 全局解释器锁
    基于Cpython，python中一个线程对应于c语言中一个线程。
    GIL会限制pyhton在同一个时刻只有哦一个线程在CPU上执行字节码,以保证线程运行安全。
    于是就无法将多个线程映射到多个CPU上执行，无法发会机器的多核优势。

    但是也不是GIL就是一直安全的，其在某些情况下也会释放。
    GIL会根据执行字节码行数或者时间片释放，以及遇到IO操作时也会主动释放。
"""
# 通过dis可以查看python程序转换成字节码的过程
import dis


def add(a):
    a += 1
    return a


if __name__ == '__main__':
    print(dis.dis(add))
