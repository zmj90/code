"""
    编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端

           服务端     接收内容 --> 写入到一个文件中

           客户端     读取图片内容  --> 发送给服务端
"""

from socket import *


class SaveImage:
    def __init__(self):
        self.len = 0
        # 创建套接字
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        # 绑定ip，端口
        self.tcp_server.bind(("192.168.0.106", 9527))
        # 创建监听
        self.tcp_server.listen(5)
        self.image_list = []

    def __receive_len(self):
        connect_socket, addr = self.tcp_server.accept()
        image_len = connect_socket.recv(128).decode()
        self.len = int(image_len)
        # print("图片长度：", self.len)
        # print("image_len类型：", type(image_len))
        connect_socket.close()

    def __receive_image(self):
        while True:
            # 创建连接
            connect_socket, addr = self.tcp_server.accept()
            data = connect_socket.recv(2048)
            # print("数据：", data)

            if len(self.image_list) == self.len:
                connect_socket.close()
                break
            else:
                self.image_list.append(data)
                # print("接收的数据列表长度：", len(self.image_list))
                # print(type(len(self.image_list)))
                # print("self.len", self.len)
                # print(type(self.len))
            connect_socket.close()

    def __write_image(self):
        connect_socket, addr = self.tcp_server.accept()
        data = connect_socket.recv(256).decode()
        # print("收到的内容：", data)
        try:
            file = open("head_img.jpg", "wb")
            for line in self.image_list:
                file.write(line)
            file.close()
            connect_socket.send("上传成功".encode())
            connect_socket.close()
        except:
            connect_socket.send("上传失败".encode())
            connect_socket.close()

    def main(self):
        self.__receive_len()
        self.__receive_image()
        self.__write_image()


if __name__ == '__main__':
    SaveImage().main()
