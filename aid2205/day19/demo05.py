"""

"""

import re

# 占有字符：匹配字符后，继续向右比较
list_result = re.findall("王者\w*","王者荣耀、刺激战场、梦幻西游")
print(list_result)
# 零宽度字符：只比较不匹配

# 至少包含一个大写字母
print(re.search(r"^(?=\w*[A-Z])\w*$", "Wgitx"))
print(re.search(r"^(?=\w*\d)\w*$", "Qi3tx"))
print(re.search(r"^(?=\w*[A-Z])(?=\w*\d)\w*$", "q5Qtx"))
# <re.Match object; span=(0, 4), match='Qitx'>


# print(re.search(r"[A-Z]\w*", "iQtx"))# Qtx
# print(re.search(r"(?=[\w*A-Z])\w*", "iQtx"))#iQtx

# 首字母必须大写
print(re.search(r"^[A-Z]\w*$", "tQx"))# Qtx
# 必须有大写
print(re.search(r"^(?=\w*[A-Z])\w*$", "tQx"))# Qtx
