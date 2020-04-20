# _*_ coding: utf-8 _*_

"""
有一个文件500G，如何读取数据？
"""


def my_readlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            # 判断是否到达文本结尾
            yield buf
            break
        buf += chunk


if __name__ == '__main__':
    with open("test.txt") as f:
        for line in my_readlines(f, "{|}"):
            print(line)
    """
    Prior to beginning tutoring sessions
    , I ask new students to fill
    , hakhhklkk
      lklk  JGDYRTYIO SKLDJ  hjjlfj.
    """
