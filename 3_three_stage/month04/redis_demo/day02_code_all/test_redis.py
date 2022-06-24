import redis

#生成连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

#基础通用命令
# key_list = r.keys("*")
#[b'u2', b'username', b'username5', b'l1', b'u1', b'u3', b'z4', b'u4']
# print(key_list)

# print(r.exists('username'))
# 存在返回1，不存在返回0
# print(r.delete('u1'))

#########list操作#########
# print(r.lpush('pyl1', 'a', 'b', 'c', 'd'))
#[b'd', b'c', b'b', b'a']
# print(r.lrange('pyl1', 0, -1))

#print(r.rpop('pyl1'))
#print(r.ltrim('pyl1', 0, 1))
#print(r.lrange('pyl1',0, -1))

#########String#########
# r.set('pys1', 'guoxiaonao')
# print(r.get('pys1'))

# r.mset({'pys2':'guo', 'pys3':'xiao'})
#[b'guo', b'xiao']
# print(r.mget('pys2','pys3'))

# print(r.incr('pys6'))
# print(r.incrby('pys6',10))


#####hash#######
#r.hset('pyh8', 'uname', 'wangweichao')
#{b'uname': b'wangweichao'}
#print(r.hgetall('pyh8'))
#r.hmset('pyh8',{'age':22,'desc':'spider'})
#print(r.hgetall('pyh8'))

