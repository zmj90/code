"""
tcp 服务端实现流程
"""

from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("localhost", 8888))

# 将套接字设置为监听套接字,监听队列大小为5
tcp_socket.listen(5)

while True:
    print("等待客户端链接....")
    # 等待处理客户端链接
    connect_socket, address = tcp_socket.accept()
    print("链接了", address, "客户端")  # 打印地址

    # 接收消息
    data = connect_socket.recv(20)
    print("接收到:", data.decode())
    n = connect_socket.send(b'Thanks')  # 发送字节串
    print("发送了%d bytes" % n)

    connect_socket.close()

# 关闭套接字
tcp_socket.close()
