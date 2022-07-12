"""
练习1:验证密码:6位,至少1个大写字母，一个下划线组成
目标字符串：Tedu_1
结果：\<re.Match object; span=(0, 8), match='Tedu_1'>

练习2:验证密码:6-12位,至少1个大写字母，1个小写字符，1个数字，
目标字符串：Tedu_123
结果：\<re.Match object; span=(0, 8), match='Tedu_123'>
"""

import re

# 6位,至少1个大写字母，一个下划线组成
print(re.search(r"^(?=[\w*A-Z])(?=\w*_)\w{6}$", "Tedu_2"))
# 6-12位,至少1个大写字母，1个小写字符，1个数字，
print(re.search(r"^(?=[\w*A-Z])(?=\w*[a-z])(?=\w*\d)\w{6,12}$", "Tedu_2"))