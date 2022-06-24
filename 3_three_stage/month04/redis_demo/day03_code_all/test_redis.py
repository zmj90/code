import redis

#生成连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

#基础通用命令
#key_list = r.keys('*')
#[b'u2', b'username', b'username5', b'l1', b'u1', b'u3', b'z4', b'u4']
#print(key_list)

#print(r.exists('u1'))
#print(r.delete('u1'))

#########list操作#########
#r.lpush('pyl1', 'a', 'b', 'c', 'd')
#[b'd', b'c', b'b', b'a']
#print(r.lrange('pyl1', 0, -1))

#print(r.rpop('pyl1'))
#print(r.ltrim('pyl1', 0, 1))
#print(r.lrange('pyl1',0, -1))

#########String#########
# r.set('pys1', 'guoxiaonao')
# print(r.get('pys1'))

#r.mset({'pys2':'guo', 'pys3':'xiao'})
#[b'guo', b'xiao']
#print(r.mget('pys2','pys3'))

#print(r.incr('pys6'))
#print(r.incrby('pys6',10))


#####hash#######
#r.hset('pyh8', 'uname', 'wangweichao')
#{b'uname': b'wangweichao'}
#print(r.hgetall('pyh8'))
#r.hmset('pyh8',{'age':22,'desc':'spider'})
#print(r.hgetall('pyh8'))

########set#########
#r.sadd('pyset1', 'tom', 'jack')
#{b'jack', b'tom'}
#print(r.smembers('pyset1'))

#r.sadd('pyset2', 'tom', 'lily', 'xixi')
#{b'tom'}
#print(r.sinter('pyset1', 'pyset2'))

#########sorted set###############

#r.zadd('pyss1', {'tom':6000,'jim':5000})
#[(b'jim', 5000.0), (b'tom', 6000.0)]
#print(r.zrange('pyss1',0,-1, withscores=True))

#print(r.zrangebyscore('pyss1', '(5000', 7500,  withscores=True))

#r.zadd('pyss2', {'tom': 8000})

#r.zinterstore('pyss3',('pyss1','pyss2'), aggregate='max')

#print(r.zrange('pyss3', 0, -1, withscores=True))


