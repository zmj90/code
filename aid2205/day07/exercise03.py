"""
    创建函数,在终端中打印矩形.
    number = int(input("请输入整数:")) # 5
    for row in range(number):
    if row == 0 or row == number - 1:
         print("*" * number)
    else:
         print("*%s*" % (" " * (number - 2)))
"""
def print_rectangular(number, char):
    for row in range(number):
        if row == 0 or row == number - 1:
            print(char * number)
        else:
            print(char + " " * (number - 2) + char)

print_rectangular(5, "*")
print_rectangular(8, "#")
print_rectangular(10, "$")

