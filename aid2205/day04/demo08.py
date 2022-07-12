"""
    切片
        定位多个元素
        容器名[整数:整数:整数]
"""
message = "我是花果山水帘洞美猴王孙悟空"
# 写法1:容器名[开始:结束:间隔]
# 注意:不包含结束
print(message[2:5:1]) # 花果山

# 写法2:容器名[开始:结束]
# 注意:间隔默认为1
print(message[2:5]) # 花果山

# 写法3:容器名[:结束]
# 注意:开始默认为开头
print(message[:5]) # 花果山

# 写法4:容器名[:]
# 注意:结束默认为最后
print(message[:]) # 我是花果山水帘洞美猴王孙悟空
print(message[-3:]) # 孙悟空

message = "我是花果山水帘洞美猴王孙悟空"
print(message[5:8]) # 水帘洞
print(message[3:-3]) #  果山水帘洞美猴王
print(message[3:-3:-1]) # 空
print(message[-3:3:-1]) # 孙王猴美洞帘水山
print(message[::2]) #  我花山帘美王悟
# 反转
print(message[::-1]) # 空悟孙王猴美洞帘水山果花是我
print(message[:99]) # 不报错








