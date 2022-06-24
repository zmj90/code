#消费者
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

while True:

    task = r.brpop('pylt1', 10)
    #task : (b'pylt1', b'sendEmail_guoxiaonao@tedu.cn_guo@tedu.cn_hahaha')
    print(task)
    if task:
        task_data = task[1]
        task_str = task_data.decode()
        task_list = task_str.split('_')
        print('--receiver task, task type is %s'%(task_list[0]))

    else:
        print('--no task---')


