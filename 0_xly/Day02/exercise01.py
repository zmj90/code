# 输入身高(m)与体重(kg)值,计算并打印BMI等级

# 写法1：
# # 1 获取用户输入的身高与体重值
# height = float(input('请输入身高（m）'))
# weight = float(input('请输入体重（kg）'))
#
# # 2 计算BMI
# # bmi = weight / height ** 2
# # # 保留1位小数
# # bmi = round(bmi, 1)
#
# bmi = round(weight / height ** 2, 1)
# print('BMI：', bmi)
#
# # 3 判断并打印bmi的范围等级
# if bmi <= 18.4:
#     print('偏瘦')
# elif 18.5 <= bmi <= 23.9:
#     print('正常')
# elif 24 <= bmi < 28:
#     print('过重')
# elif bmi >= 28:
#     print('肥胖')
# else:
#     print('bmi值错误')


height = float(input('请输入身高（m）'))
weight = float(input('请输入体重（kg）'))

# 保证身高与体重值正确，则BMI值正确
if height > 0 and weight > 0:
    bmi = round(weight / height ** 2, 1)
    print('BMI：', bmi)

    if bmi <= 18.4:
        print('偏瘦')
    elif bmi <= 23.9:
        print('正常')
    elif bmi < 28:
        print('过重')
    # elif bmi >= 28:
    else:  # bmi >= 28
        print('肥胖')
else:
    print('身高与体重值错误')