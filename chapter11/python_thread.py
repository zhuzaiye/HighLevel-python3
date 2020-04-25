# _*_ coding: utf-8 _*_

"""
线程：
    操作系统能够操控的最小单元是“线程”。

    对于IO操作来说，多线程和多进程性能差别不大。
"""

import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


# 也可以继承threading.Thread类进行多线程编程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    # 重载run方法，不要重载start方法
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    # 重载run方法，不要重载start方法
    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == '__main__':
    # th1 = threading.Thread(target=get_detail_html, args=("",))
    # th2 = threading.Thread(target=get_detail_url, args=("",))

    th1 = GetDetailHtml("get detail Html")
    th2 = GetDetailUrl("get detail Url")

    # 如何使得main_thread退出，子线程就会被kill
    # setDaemon将子线程设为守护线程
    # th1.setDaemon(True)
    # th2.setDaemon(True)

    start_time = time.time()
    th1.start()
    th2.start()

    # join的方法来阻塞主线程，来等待子线程全部运行完后在运行主线程
    th1.join()
    th2.join()

    # 需求 1：main_thread 退出时，需要kill子线程
    # 需求 2：main_thread必须等待所有子线程运行完在结束自己，这个时候就需要join方法
    print("last time: {}".format(time.time() - start_time))

    """
    get detail html started
    get detail url started
    last time: 0.009032964706420898 # main_thread已经结束，但是子线程仍在运行，这引出需求1
    get detail url end
    get detail html end
    """

    """
    get detail html started
    get detail url started
    last time: 0.0009953975677490234
    """

    """
    get detail html started
    get detail url started
    get detail html end
    get detail url end
    last time: 4.014985084533691  #  时间是最长的那个，当然会加上主线程时间，说明是并发的
    """
