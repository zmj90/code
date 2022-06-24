from socket import *

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(("localhost", 14443))  # 绑定ip，端口
tcp_server.listen(5)  # 创建监听

# 第一次接收图片长度
connect_socket, addr = tcp_server.accept()
image_lencount = connect_socket.recv(128).decode()
print(image_lencount)
connect_socket.close()

# 第二次存储图片内容
image_list = []
while True:
    connect_socket, addr = tcp_server.accept()
    data = connect_socket.recv(2048)
    if len(image_list) == int(image_lencount):
        connect_socket.close()
        break
    else:
        image_list.append(data)
    connect_socket.close()

# 第三次写入图片，返回消息
connect_socket, addr = tcp_server.accept()
data = connect_socket.recv(256)
print("收到的内容", data)
file = open("head_img.jpg", "wb")
try:
    for line in image_list:
        file.write(line)
    file.close()
    n = connect_socket.send(b"upload success")
except:
    n = connect_socket.send(b"upload failed")
connect_socket.close()

tcp_server.close()
