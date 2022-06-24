# 练习2：输入一个成绩，判断在哪个等级并打印
# [0, 60)   E等级
# [60, 70)   D等级
# [70, 80)   C等级
# [80, 90)    B等级
# [90, 100]   A等级

score = int(input('请输入一个成绩：'))

if 0 <= score < 60:
    print('E等级')
elif 60 <= score < 70:
    print('D等级')
elif 70 <= score < 80:
    print('C等级')
elif 80 <= score < 90:
    print('B等级')
elif 90 <= score <= 100:
    print('A等级')
else:
    print('成绩输入错误')


