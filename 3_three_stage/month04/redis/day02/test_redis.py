import redis


r = redis.Redis(host="127.0.0.1",
                port="6379", db=0,
                password="123456",
                decode_responses=True
                )
"""
    day03
"""
# r.sadd('pyset1', 'tom', 'jack')
# print(r.smembers('pyset1'))

# r.sadd("pyset2", "tom", "lily", "luxi")
# print(r.smembers('pyset2'))

# print(r.sinter("pyset1", "pyset2"))

# r.zrangebyscore()
# r.zinterstore()









"""
    day02
"""

# key_list = r.keys("*")
# print(key_list)
# # [b'username', b'trill:username']

# re = r.exists("username")
# print(re)
# # 1

# r.lpush("l1", 'a', 'b', 'c', 'd')
# print(r.lrange("l1", 0, -1))
# # [b'd', b'c', b'b', b'a']

# r.set("l2", "zmj")
# print(r.get("l2"))

# r.mset({"l3":1, "l4":2})
# print(r.mget("l3", "l4"))

# print(r.incr("l5"))

# print(r.hset("pyh1", "uname", "zmj"))
# print(r.hgetall("pyh1"))
