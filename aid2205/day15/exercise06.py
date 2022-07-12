"""
练习1：定义函数,在列表中找出所有偶数
    [43,43,54,56,76,87,98]

练习2：定义函数,在列表中找出所有数字
    [43,"悟空",True,56,"八戒",87.5,98]
"""
list01 = [43, 43, 54, 56, 76, 87, 98]
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def find_all_even():
    for item in list01:
        if item % 2 == 0:
            yield item

def find_all_number():
    for item in list02:
        # if type(item) == int or type(item) == float:
        if type(item) in (int,float):
            yield item

# 调用函数不执行,返回的是生成器对象
result = find_all_even()
# 依靠for循环执行
for even in result:
    print(even)

# for + 调用函数才执行
for item in find_all_number():
    print(item)