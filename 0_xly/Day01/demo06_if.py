# if语句

# # 需求1：判断输入的是男
# gender = input('请输入性别：')
# if gender == '男':
#     print('您好，先生')


# # 需求2：判断输入的是男、女
# gender = input('请输入性别：')
# if gender == '男':
#     print('您好，先生')
# else:  # 否则，gender == '女'
#     print('你好，女士')


# # 需求3：判断输入的是男、女、未知
# gender = input('请输入性别：')
# if gender == '男':
#     print('您好，先生')
# elif gender == '女':
#     print('你好，女士')
# else:  # 否则，gender 未知
#     print('性别未知')


# 需求4：输入一个数，判断是否大于20 30 40 50 60
number = int(input('请输入一个数：'))

if number > 20:
    print('大于20')
elif number > 30:
    print('大于30')
elif number > 40:
    print('大于40')
elif number > 50:
    print('大于50')
elif number > 60:
    print('大于60')
else:
    print('数错误')