"""
    消费者
"""

import redis

r = redis.Redis(host="127.0.0.1", port="6379", db=0, decode_responses=True)

while True:
    task = r.brpop("l1", 30)
    # print(task)
    # ('l1', 'sendmail#qwe@tedu.cn#asd@tedu.cn#hello world')
    task_list = task[1].split("#")
    # print(task_list)
    if task_list[0] == "sendmail":
        pass