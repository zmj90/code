import redis
import time


pool = redis.ConnectionPool(host='127.0.0.1', db=1, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)

def double_account(user_id):

    key = 'account_%s'%(user_id)
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                #pipe.watch命令 调用后 即刻发给服务器
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                print('--new value is %s'%(value))
                print('--sleep is start')
                time.sleep(20)
                print('--sleep is over')

                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except redis.WatchError:
                print('---value changed')
                continue

    return int(r.get(key))


if __name__ == '__main__':
    #account_guoxiaonao
    print(double_account('guoxiaonao'))





