"""
客户端
"""
from socket import *
from multiprocessing import Process


class WordSelect:
    def __init__(self, socket_IP: str, socket_port: int):
        self.socket = socket()
        print("连接服务端")
        self.socket.connect((socket_IP, socket_port))

    def start(self):
        while True:
            if not self.log_in(): break
            self.select_word()

    def log_in(self):
        """
        登陆和注册
        """
        respond = (self.socket.recv(50).decode()).split(' ', 1)
        if respond[0] == 'ok':
            print(respond[1])
            count = 0
            while count < 5:
                count += 1
                user = input("请登陆/或输入 up 注册\n输入用户名/up >>>")
                if user == 'up':
                    if self.log_in_user():
                        continue
                    else:
                        return False
                elif self.landing(user):
                    return True
            else:
                self.socket.close()
                print("登陆次数超量，已断开连接")
                return False
        else:
            pass

    def log_in_user(self):
        """
        注册用户 A
        """
        count = 0
        while count < 5:
            count += 1
            new_user = input('请输入用户名，输入 up 返回登陆界面 >>>')
            if new_user == 'up': return True
            password = input("请输入密码>>>")
            self.socket.send(('A ' + new_user + ' ' + password).encode())
            respond = self.socket.recv(50).decode().split(' ', 1)
            if respond[0] == 'ok':
                print(respond[1])
                return True
            else:
                print(respond[1])
        else:
            self.socket.close()
            print("注册次数超量，已断开连接")
            return False

    def landing(self, user):
        """
        登陆 P
        :param user: 用户名
        """
        password = input("请输入密码>>>")
        self.socket.send(f"P {user} {password}".encode())
        respond = self.socket.recv(50).decode().split(' ', 1)
        print(respond)
        if respond[0] == 'ok':
            print(respond[1])
            return True
        else:
            print(respond[1])
            return False

    def select_word(self):
        """
        接收单词 S
        注销 Q
        """
        while True:
            word = input("请输入要查询的单词,输入 Q 注销登陆>>>")
            if word == 'Q':
                self.socket.send(word.encode())
                break
            self.socket.send(('S ' + word).encode())
            respond = self.socket.recv(1024).decode().split(" ", 1)
            if respond[0] == 'ok':
                print(f'{word}>>>{respond[1]}')
            else:
                print(respond[1])

abc = WordSelect('127.0.0.1',12345)
abc.start()