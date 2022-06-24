"""
服务器端
"""

from socket import *
from select import *
from typing import Tuple
from multiprocessing import Pool, Process
from signal import *
import Database_connect
import re


class WordSelect:
    def __init__(self, database_name: str, database_password: str, socket_IP: str, socket_port: int,
                 word_addr='dict.txt'):
        """
        :param database_name: 数据库名字
        :param database_password: 数据库密码
        :param socket_IP: 套接字IP
        :param socket_port: 套接字端口
        :param word_addr: 单词表地址
        """
        self.socket = socket()
        self.socket.bind((socket_IP, socket_port))
        self.database = Database_connect.Database(database_name, database_password)
        self.ep = epoll()
        self.dict_IO = {}
        self.word_addr = word_addr

    def start(self):
        self.set_up_tables()
        self.up_word()
        self.wait_connect()

    def set_up_tables(self):
        """
        创建用户表，和单词表
        """
        sql_table_user = 'CREATE TABLE user (uid mediumint unsigned auto_increment primary key,u_name varchar(20) unique not null ,password varchar(20) not null )'
        sql_table_word = 'CREATE TABLE words(uid mediumint unsigned auto_increment primary key, word varchar(50) unique not null, meaning varchar(1024))'
        try:
            self.database.cur.execute(sql_table_user)
            self.database.cur.execute(sql_table_word)
            self.database.db.commit()
        except:
            self.database.db.rollback()

    def wait_connect(self):
        self.socket.listen()
        self.socket.setblocking(False)
        self.dict_IO[self.socket.fileno()] = self.socket
        self.ep.register(self.socket, EPOLLIN)
        # pool = Pool(2)
        signal(SIGCHLD, SIG_IGN)
        while True:
            events = self.ep.poll()
            for fd, event in events:
                if fd == self.socket.fileno():
                    # Process(target=self.user_connect, args=(self.dict_IO[fd],)).start()
                    # 子进程貌似不能处理IO多路复用触发的IO事件，猜测是当把处理流程放到子进程之后，在子进程还没来得及处理的时候，主进程又重新监控了IO，主进程就会认为这个IO没有被处理，就会再次触发，恶性循环
                    print("有客户端连接")
                    # print("正在处理客户端连接")
                    self.user_connect(self.dict_IO[fd])
                    # connect, addr = self.dict_IO[fd].accept()
                    # connect.setblocking(False)
                    # self.dict_IO[connect.fileno()] = connect
                    # self.ep.register(connect, EPOLLIN)
                    # self.respond_home(connect)
                    # print("已处理客户端连接")
                else:
                    # Process(target=self.request_discern, args=(self.dict_IO[fd],)).start()
                    self.request_discern(self.dict_IO[fd])
                    print('有新消息')

    def user_connect(self, socket):
        """
        处理用户连接
        """
        print("正在处理客户端连接")
        connect, addr = socket.accept()
        connect.setblocking(False)
        self.dict_IO[connect.fileno()] = connect
        self.ep.register(connect, EPOLLIN)
        self.respond_home(connect)
        print("已处理客户端连接")

    def up_word(self):
        """
        上传单词,如果更换单词本，需要重新配置正则表达式
        """
        if input("第一次使用请往数据库上传单词表\n  键入 up 上传，其余皆为跳过 >>>") == 'up':
            sql_insert = 'insert into words(word, meaning) values (%s,%s)'
            file = open(self.word_addr, 'r')
            pattern = r"\S+| \S.*"
            count = 0
            while True:
                message = file.readline()
                if message:
                    try:
                        word, mean = re.findall(pattern, message)
                    except ValueError:
                        word = re.findall(pattern, message)[0]
                        self.database.cur.execute('insert into words(word) values (%s)', args=(word,))
                        self.database.db.commit()
                        count += 1
                        continue
                    try:
                        self.database.cur.execute(sql_insert, args=(word, mean))
                        self.database.db.commit()
                        count += 1
                    except:
                        self.database.db.rollback()
                else:
                    break
            file.close()
            print(f"本次新上传{count}个单词")

    def word_select(self, word, connect):
        """
        查询单词解释
        :param word: 单词
        """
        sql_select = 'select meaning from words where word = %s'
        self.database.cur.execute(sql_select, args=(word,))
        mean = self.database.cur.fetchone()  # type:Tuple[str]
        if mean:
            connect.send(('ok ' + mean[0]).encode())
        else:
            connect.send('no 没有这个单词'.encode())

    def request_discern(self, connect: socket):
        # request = connect.recv(2048).decode().split('\n')
        # request_head, request_body = request[0].split(' '), request[-1].split(' ')
        # if request_head[0] == 'GET':
        #     if request_head[1] == '/':
        #         self.respond_home(connect)
        # else: # 只会 GET
        #     pass
        request = connect.recv(80).decode().split(" ", 1)
        print(request)
        if request[0] == 'S':  # 查询单词
            self.word_select(request[1], connect)
        elif request[0] == 'A':  # 添加用户
            self.add_user(request[1], connect)
        elif request[0] == 'Q':  # 用户注销
            self.down_user(connect)
        elif request[0] == 'P':  # 用户登陆
            self.up_user(request[1], connect)
        elif not request[0]:
            self.ep.unregister(connect.fileno())
            del self.dict_IO[connect.fileno()]
            connect.close()

    def respond_home(self, connect: socket):
        """
        主页，就算是吧
        :param connect: 套接字
        """
        connect.send('ok welcome to word dict!'.encode())

    def add_user(self, user_passwprd, connect):
        """
        注册用户
        :param user_passwprd: 申请注册的用户和密码
        :param connect: 套接字
        """
        user, passwprd = user_passwprd.split(' ', 1)
        sql_add_user = 'insert into words.user(u_name, password) values (%s,%s)'
        try:
            self.database.cur.execute(sql_add_user, args=(user, passwprd))
            self.database.db.commit()
            connect.send('ok 注册成功'.encode())
        except:
            self.database.db.rollback()
            connect.send('no 用户非法，注册失败'.encode())

    def down_user(self, connect):
        """
        用户下线
        :param connect: 套接字
        """
        connect.send('888888'.encode())
        self.ep.unregister(connect.fileno())
        del self.dict_IO[connect.fileno()]
        connect.close()

    def up_user(self, user_passwprd, connect):
        """
        用户登陆
        :param user_passwprd: 等待验证的登陆用户名和密码
        :param connect: 套接字
        """
        user, passwprd = user_passwprd.split(' ', 1)
        sql_up_user = 'select password from words.user where u_name = %s '
        self.database.cur.execute(sql_up_user, args=(user,))
        try:
            if self.database.cur.fetchone()[0] == passwprd:
                connect.send("ok welcome".encode())
            else:
                connect.send("no 用户非法".encode())
        except:
            connect.send("no 用户非法".encode())


abc = WordSelect('words', 'mu7401889', '0.0.0.0', 12345)
abc.start()
