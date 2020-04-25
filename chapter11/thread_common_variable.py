# _*_ coding: utf-8 _*_

"""
线程间的通信： 共享变量

线程间通讯方式：
    1、共享变量  -- 线程共享变量不安全，也就是说线程之间不安全
    2、于是可以通过加锁的方式来保证共享变量的线程之间的安全。
"""
import time
import threading

# 设定一个爬虫模拟
# 首先get_detail_url获取文章的列表页，解析出文章内容详情的url
# 然后get_detail_html拿到内容详情url进行抓取内容

# 1 首先设定一个共享列表
detail_url_list = []


def get_detail_html(detail_url_list):
    """
    爬取文章内容详情
    """
    # global detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


#
def get_detail_url(detail_url_list):
    """
    爬取文章列表页,较获取内容详情来说很快
    """
    # global detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == '__main__':
    th1 = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    # 开启多个获取详情内容的线程
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()

    start_time = time.time()
    print("last time: {}".format(time.time() - start_time))