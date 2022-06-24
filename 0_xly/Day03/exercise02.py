# 练习1：猜拳小游戏
# 电脑随机出：石头、剪刀、布，用户也是输入：石头剪刀布，每次打印：电脑出：xxx，用户出：xxx, xxx赢了，最终打印：电脑与用户各赢多少局。

import random

lists = ["石头", '剪刀', "布"]

#           用户出的  电脑出的
user_win = [['石头', '剪刀'],
            ['布', '石头'],
            ['剪刀', '布']]

comp_win = [['石头', '布'],
            ['布', '剪刀'],
            ['剪刀', '石头']]

uwin_times = 0    # 记录用户赢的次数
cwin_times = 0    # 记录电脑赢的次数

while True:
    user = input('请输入【石头剪刀布】:')
    # 用户输入为空或者用户输入的不是石头剪刀布则结束
    if user == '' or user not in lists:
        print('电脑赢了{}局，用户赢{}局'.format(cwin_times, uwin_times))
        break

    # 随机值对应列表的索引值 [0, 1, 2]
    index = random.randint(0, 2)
    print(index, lists[index])

    # [用户出的, 电脑出的]
    res = [user, lists[index]]

    if res in user_win:
        uwin_times += 1
        print('电脑出：{}，用户出：{}, {}赢了'.format(lists[index], user, '用户'))
    elif res in comp_win:
        cwin_times += 1
        print('电脑出：{}，用户出：{}, {}赢了'.format(lists[index], user, '电脑'))
