# 现有资产10亿，每天花费1半，问多少天可以花完（小于1当花完）

money = 1000000000
day = 0   # 记录天数

while money > 1:
    # money = money / 2
    money /= 2   # 每天花一半
    day += 1   # 天数+1
    print('第', day, '天，剩余：', money)