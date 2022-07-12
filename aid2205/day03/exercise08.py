"""
    练习3：
    在终端中循环录入5个成绩,
    最后打印平均成绩(总成绩除以人数)
"""
count = 0
total_score = 0
while count < 5:
    total_score += int(input("请输入成绩:"))
    count += 1
print("平均成绩:" + str(total_score / 5))
# 练习4：
# 一张纸的厚度是0.01毫米
# 请计算，对折多少次超过珠穆朗玛峰(8844.43米)