"""
    异常处理
        适用性：逻辑错误,而非语法错误
        目的：由异常状态改为正常状态
               向上翻     向下走
        核心价值：保障程序能够按照既定流程执行，不紊乱。

"""
# 语法错误
# print(qtx)
# print(1 + "1")
# ...

# 逻辑错误
"""
def div_apple(apple_count): # 3
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count / person_count
    print(f"每人{result}个苹果")

def main(): # 2
    div_apple(10)

main() # 1
print("后续逻辑")
"""


def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except Exception:
        print("分苹果失败了")

div_apple(10)
print("后续逻辑")