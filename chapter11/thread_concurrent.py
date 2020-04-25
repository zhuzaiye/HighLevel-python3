# _*_ coding: utf-8 _*_

"""
concurrent

1、线程池
    主线程可以后去某一线程的状态还活着某一个任务的状态，以及返回值。
    当一个线程完成的时候，主线程能立即知道。
    futures可以让多线程和多进程编码接口一致。

2、
    class ThreadPoolExecutor(_base.Executor):

    # Used to assign unique thread names when thread_name_prefix is not supplied.
    _counter = itertools.count().__next__

    def __init__(self, max_workers=None, thread_name_prefix=''):
        Initializes a new ThreadPoolExecutor instance.

        Args:
            max_workers: The maximum number of threads that can be used to
                execute the given calls.
            thread_name_prefix: An optional name prefix to give our threads.

"""

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)

    # 通过submit函数提交执行的函数到线程池，submit非阻塞，立即返回u
    task1 = executor.submit(get_html, 3)  # 返回是一个future对象
    task2 = executor.submit(get_html, 2)

    # done方法用于判定某个任务是否完成
    print(task1.done())
    time.sleep(3)
    print(task1.done())

    # result方法可以获取task任务的执行结果
    print(task1.result())

    # 获取已经完成的task的返回
    urls = [2, 3, 4]
    all_task = [executor.submit(get_html, url) for url in urls]
    for future in as_completed(all_task):  # 这个是谁先完成输出谁
        data = future.result()
        print("get {} page success".format(data))

    # 通过executor获取已经完成的task
    for data in executor.map(get_html, urls):
        print("get {} page success".format(data))  # 按照urls顺序输出

    # wait 方法指定的线程完成钱阻塞当前主线程
    wait(all_task, return_when="FIRST_COMPLETED")
    print("the main thread done")
