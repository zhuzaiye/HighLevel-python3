# _*_ coding: utf-8 _*_

"""
线程同步机制：
    1、threading --> Lock 会影响并发性能
    2、lock --> 会出现死锁 比如资源竞争出现互相等待造成的死锁
    3. Relock 重复锁使用
"""

import dis
import threading

total = 0
lock = threading.Lock()


def add1():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


if __name__ == '__main__':
    # print(dis.dis(add1))

    th1 = threading.Thread(target=add1)
    th2 = threading.Thread(target=desc)
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print(total)

"""
add1字节码执行顺序：
    0 LOAD_FAST                0 (a)  load 方法 a
    2 LOAD_CONST               1 (1)  load 变量 1
    4 INPLACE_ADD                     实现 加法 +
    6 STORE_FAST               0 (a)  保存
    8 LOAD_CONST               0 (None)
    10 RETURN_VALUE
    
由于GIL在一段字节码执行完毕后，是有可能释放的，切换到另外线程，
这就为线程共享提供共同修改一个变量的可能。
"""
