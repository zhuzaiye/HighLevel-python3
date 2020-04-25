# _*_ coding: utf-8 _*_

"""
threading.Semaphore 用于控制线程数量的锁
    比如说写和读，读多次，写的少

    Semaphore仍是采用condition方法
    acquire开启一个线程就加1，但是必须释放
    release接收一个增加线程执行后，就必须释放该线程，减1
"""

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("get html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("http://www.baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    # 每三个进行组合执行
    url_producer = UrlProducer(sem)
    url_producer.start()
