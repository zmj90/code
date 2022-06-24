# if语句嵌套
score = int(input('请输入一个成绩：'))

# 情况1：成绩正确：[0,100]
if 0 <= score <= 100:
    if score < 60:  # [0, 60)
        print('E等级')
    elif score < 70:  # [60, 70)
        print('D等级')
    elif score < 80:  # [70, 80)
        print('C等级')
    elif score < 90:  # [80, 90)
        print('B等级')
    elif score <= 100:  # [90, 100]
        print('A等级')
else:  # 情况2：不在[0,100]
    print('成绩输入错误')
