"""
    异常处理各种写法
"""
# 写法1:包治百病
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    # except Exception:
    except:
        print("分苹果失败了")

div_apple(10)
print("后续逻辑")

# 写法2:对症下药
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except ValueError:
        print("输入的不是整数")
    except ZeroDivisionError:
        print("分母不能是0")

div_apple(10)
print("后续逻辑")
"""

# 写法3:无论是否发生异常,一定执行的任务
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
        # 文件操作
        # 1. 打开文件
        # 2. 读写文件
    finally:
        # 3. 关闭文件(必须执行)
        print("分苹果结束")

div_apple(10)
print("后续逻辑")
"""