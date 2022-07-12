"""
    匹配位置-验证
"""
import re

# 验证
# 输入的单词首字母必须大写
print(re.search(r'^[A-Z][a-z]*',"This") != None)

# 命名必须以Model结尾
# 具有^$语义：必须是
# 没有^$语义：包含
print(re.search(r'^.+Model$',"StudentModel"))

# 单词边界
print(re.findall(r'\bis\b',"This is a test'is"))
# ['is']

# 验证数值类型(整数、小数)
print(re.search("^\d+\.?\d+$","1.0"))

# 中间的点表达任意字符
# print(re.search("^\d+.?\d+$","1#0"))
