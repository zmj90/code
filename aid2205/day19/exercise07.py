"""
    练习：书名号内保留第一个字符
    目标字符串：《Python编程快速上手》,《Python编程无师自通》,《利用Python进行数据分析》
    结果：《P\*》,《P\*》,《利*》
"""
import re

# \g<1>
str_result = re.sub(
    r"《(.).*?》",
    "《\g<1>*》",
    "《Python编程快速上手》,《Python编程无师自通》,《利用Python进行数据分析》"
)
print(str_result)


content = """
15:23
20,16
20 16
"""
# \g<1>
str_result = re.sub(r"(\d{2})[:,\s](\d{2})",
                    "\g<1>:\g<2>",content)
print(str_result)