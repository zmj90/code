"""
    for 循环计数
"""
# 引入
# count = 0  # 开始
# while count < 3:  # 结束
#     print("跑圈")
#     count += 1  # 间隔

# 开始,结束,间隔
# 写法1:range(开始,结束,间隔)
# 注意:不包含结束值
for count in range(0,3,1):
    print(count)

# 写法2:range(开始,结束)
# 注意:间隔默认为1
for item in range(0,3):
    print(item)

# 写法3:range(结束)
# 注意:开始默认为0
for number in range(3):# 0 1 2
    print(number)
