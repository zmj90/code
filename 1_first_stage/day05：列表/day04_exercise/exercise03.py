"""
5.在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上
"""

message = "上海自来水来自海上"
if message == message[::-1]:
    print("是回文")
else:
    print("不是回文")
