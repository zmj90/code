# 将names=['中国移动','中国联通', '中国电信'], phone=[10086, 10010, 10000] 转换为字典 {'中国移动':10086,'中国联通':10010, '中国电信':10000}

# 共同点：长度一致

names = ['中国移动', '中国联通', '中国电信']
phone = [10086, 10010, 10000, 100002, 100034]

# 假设法
# 假设名字列表长度最短
min_length = len(names)
phone_len = len(phone)
# 如果手机号列表比名字列表长度还小，则最短是手机号列表长度
if min_length > phone_len:
    min_length = phone_len

dicts = {}

for i in range(min_length):
    # print(names[i], phone[i])
    dicts[names[i]] = phone[i]

print(dicts)