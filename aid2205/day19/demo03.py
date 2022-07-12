"""
    分组
"""
import re

list_result = re.findall(r'(\d{3})-(\d{8})',"座机：010-66073788。")

# ['张无忌,赵敏', '张翠山,殷素素']
list_result = re.findall(r'<(.+?)>',"<张无忌,赵敏>,周芷若,<张翠山,殷素素>,小昭")
print(list_result)