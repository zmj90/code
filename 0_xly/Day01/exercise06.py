# ​	输入体重（kg）与身高（m），计算并打印 BMI（身体健康指数）
# ​	BMI = 体重 / 身高 的平方

weight = float(input('请输入体重（kg）:'))
height = float(input('请输入身高（m）:'))

bmi = weight / (height ** 2)

# 设置结果保留的位数：1     16:40 上课
bmi = round(bmi, 1)

print('BMI是：', bmi)
