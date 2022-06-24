"""
    生产者
"""

import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

s = "sendmail#qwe@tedu.cn#asd@tedu.cn#hello world"
r.lpush("l1", s)
