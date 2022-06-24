# 函数定义

# # 形式1：函数无参数
# # 需求1：第2 第3 第1 释放技能
# # - 函数定义者
# def skill():
#     '''
#       释放技能
#     :return: None
#     '''
#     print('释放2技能')
#     print('释放3技能')
#     print('释放1技能')
#     print('释放1技能')
#     print('释放2技能')
#
# # 函数调用 - 函数使用者
# skill()
# skill()



# # 形式2：函数有参数
# # 需求2：第2 第3 第1 释放技能
# # - 函数定义者
# def skill(n):  # n 形式参数-n=5
#     '''
#         释放技能
#     :param n: 释放次数
#     :return: None
#     '''
#     for i in range(n): # n=5
#         print('释放2技能')
#         print('释放3技能')
#         print('释放1技能')
#
# # 函数调用 - 函数使用者
# skill(5)
# # 查看文档字符串
# print(skill.__doc__)



# 形式3：函数有返回值
# 需求3：第2 第3 第1 释放技能，返回："冷却中"
# - 函数定义者
def skill(n):  # n 形式参数-n=5
    '''
        释放技能
    :param n: 释放次数
    :return: None
    '''
    for i in range(n): # n=5
        print('释放2技能')
        print('释放3技能')
        print('释放1技能')
    # return '冷却中'
    return 123, 'OK'
    # print('函数调用结束...')  # 不执行

# 函数调用 - 函数使用者
res = skill(5)
print('函数返回的结果：', res)