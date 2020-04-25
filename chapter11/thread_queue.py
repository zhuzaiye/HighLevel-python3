# _*_ coding: utf-8 _*_

"""
线程间通信： queue

    通过消息队列实现线程通信
    queue是线程安全的，因为你就是实现的deque，内部已经线程安全
"""
import time
import threading
from queue import Queue


def get_detail_html(queue):
    """
    爬取文章内容详情
    """
    # global detail_url_list
    while True:
        url = queue.get()  # 如果为空，会实现阻塞
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


#
def get_detail_url(queue):
    """
    爬取文章列表页,较获取内容详情来说很快
    """
    # global detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))  # 如果已满，也会阻塞等待
        print("get detail url end")


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    th1 = threading.Thread(target=get_detail_url, args=(detail_url_queue,))

    # 开启多个获取详情内容的线程
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()
    print("last time: {}".format(time.time() - start_time))
