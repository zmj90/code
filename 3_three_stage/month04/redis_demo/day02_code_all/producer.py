#生产者
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 任务类别/收件人/发件人/内容
s = '%s_%s_%s_%s'%('sendEmail', 'guoxiaonao@tedu.cn', 'guo@tedu.cn','hahaha')

#任务发到redis的原则  先进先出[lpush, brpop]
r.lpush('pylt1', s)