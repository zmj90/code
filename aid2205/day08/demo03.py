"""
    跨函数调用
"""


# -----------------定义函数----------------------

def attack_single():  # 3
    print("直拳")
    print("摆拳")
    print("勾拳")
    return "ok"

def attack_repeat(count):  # 2
    list_result = []
    for number in range(count):
        data = attack_single()
        list_result.append(data)
    return list_result

# -----------------调用函数----------------------
print(attack_repeat(2))  # 1
