# _*_ coding: utf-8 _*_

"""
threading.Condition:
    条件变量，用于复杂的线程间同步
    wait
    notify

    wait 方法必须放在acquire之后或者在with之后才能执行，否则会报错

    condition有两把锁，底层锁和wait中的锁，notify会释放waiter队列中添加的锁
"""
import threading


class XiaoAI(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小艾")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 好啊".format(self.name))
            self.cond.notify()


class TianAI(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}: 你好".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 来玩吧".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()
    x = XiaoAI(cond)
    t = TianAI(cond)

    # 启动顺序很重要
    # t.start()
    x.start()
    t.start()

    #
    """
    天猫: 你好
    小艾: 在
    天猫: 来玩吧
    小艾: 好啊
    """
