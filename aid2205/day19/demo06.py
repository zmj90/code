"""
    替换
"""
import re

content = """
15:23
20,16
20 16
"""
# \g<1>
str_result = re.sub(r"(\d{2})[:,\s](\d{2})",
                    "\g<1>:\g<2>",content)
print(str_result)