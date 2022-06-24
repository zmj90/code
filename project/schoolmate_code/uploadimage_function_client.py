from socket import *


class UploadImage:
    def __init__(self):
        self.server_address = ("192.168.0.106", 9527)  # 定义服务器ip地址
        # 创建套接字

    def __send_image_len(self, file_name):
        tcp_client = socket(AF_INET, SOCK_STREAM)
        tcp_client.connect(self.server_address)
        image_len = len(self.__read_image(file_name))
        tcp_client.send(str(image_len).encode())
        tcp_client.close()

    def __upload_image(self, filename):
        image_len = len(self.__read_image(filename))
        print(image_len)
        i = 0
        while True:
            tcp_client = socket(AF_INET, SOCK_STREAM)
            tcp_client.connect(self.server_address)  # 连接服务端
            data = self.__read_image(filename)
            # print("数据", data)
            # print("index", i)
            if i < image_len:
                tcp_client.send(data[i])
                i += 1
            else:
                break
            tcp_client.close()
        # data = tcp_client.recv(256)
        # print(data.decode())

    def __receiver_msg(self):
        tcp_client = socket(AF_INET, SOCK_STREAM)
        tcp_client.connect(self.server_address)
        tcp_client.send("传输完成".encode())
        data = tcp_client.recv(256)
        print(data.decode())
        tcp_client.close()

    def __read_image(self, file):
        data = open(file, "rb")
        return data.readlines()

    def main(self, file):
        self.__send_image_len(file)
        self.__upload_image(file)
        self.__receiver_msg()


if __name__ == '__main__':
    UploadImage().main("sjch.jpg")
