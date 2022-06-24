from socket import *

server_address = ("localhost", 14443)  # 定义服务器ip地址

# 第一次连接，发送图片长度
tcp_client = socket(AF_INET, SOCK_STREAM)  # 创建套接字
tcp_client.connect(server_address)
data = open("./风景.jpg", "rb")
file = data.readlines()
image_len = len(file)
tcp_client.send(str(image_len).encode())
tcp_client.close()
print(len(file))


# 第二次连接，发送图片内容
list_len = len(file)
i = 0
while True:
    tcp_client = socket(AF_INET, SOCK_STREAM)
    tcp_client.connect(server_address)  # 连接服务端
    data = file
    if i < list_len:
        print(i)
        tcp_client.send(data[i])
        i += 1
    else:
        break
    tcp_client.close()


# 第三次连接，发送传输完成
tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(server_address)
n = tcp_client.send(b"trans finish")
data = tcp_client.recv(256)
print("收到的内容", data)
tcp_client.close()
