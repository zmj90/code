"""

"""
list_name = ["文杨洁", "王利花", "李杨"]
list_age = [26, 36, 35]
# 定义函数,在list_name中查找所有姓名是3个字的名称
def get_names_len_3():
    for item in list_name:
        if len(item) == 3:
            yield item

for item in get_names_len_3():
    print(item)
# 生成器 转换为 容器
list_result = list(get_names_len_3())
print(list_result)

# 定义函数,在list_age中查找大于30的第一个年龄
def get_age_gt_30():
    for item in list_age:
        if item>30:
            return item

print(get_age_gt_30())
