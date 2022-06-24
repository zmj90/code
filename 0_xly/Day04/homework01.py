# 循环录入学生的姓名与成绩，当名字输入为空则结束录入，每行打印每个学生的姓名与成绩，如果名字存在，则提示：已录入。

# 1 创建空字典：{名字：成绩}
dict_stu = {}

# 2 未知循环次数
while True:
#　　1 输入名字
    name = input('请输入名字：')

    # 判断为空，结束
    if name == '':
        break

#   2 判断名字是否存在，存在提示已录入[key唯一]
    if name in dict_stu:
        print('已录入')
        continue   # 跳过本次循环，继续新的一次循环

#   3 录入成绩（int)
    score = int(input('请输入成绩：'))

#   4 存储至字典中：stu[name] = score
    dict_stu[name] = score

    print(dict_stu)

# 3 将字典中的数据遍历
for n, s in dict_stu.items():
    print('姓名是：{},成绩是：{}'.format(n, s))