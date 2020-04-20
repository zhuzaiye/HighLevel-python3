# _*_ coding: utf-8 _*_

"""
socket运行
----------
    server端
    socket --
           --> bind -- 协议 地址 端口
                    --> listen -- 监听客户端socket请求 持续监听
                               --> accept --                                                  client端
                                          --                                                  new_socket --
                                          --> 阻塞等待连接请求(新套接字)--        <--三次握手--                --> connect() --
                                            |                    --> recv()--    < ---- 1-----------                     --> send()--
                                            |      <-----------            --> send()--     ----------2----------->                --> recv()--
                                                                                    --> close()     <----------3------------                 --> close()

"""

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        if data.decode("utf8") == "exit":
            break
        re_data = input()
        sock.send(re_data.encode("utf8"))
    sock.close()


# 从客户端获取数据
# data = sock.recv(1024)
# print(data.decode("utf8"))
# sock.send("Hi".encode("utf8"))
# server.close()
# sock.close()

# 实现聊天功能
while True:
    sock, addr = server.accept()

    # 用线程去处理新接收的连接(用户)
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))
    # server.close()
    # sock.close()
