"""
    字符串字面值
"""

# 1. 双引号
name1 = "彭文韬"
# 2. 单引号
name2 = '彭文韬'
# 3. 三引号:可见即所得到
name3 = """彭文韬"""
name3 = '''
彭
    文
        韬
'''
print(name3)
# 注意：引号冲突
message1 = '我是"花果山"水帘洞美猴王孙悟空'
message2 = "我是'花果山'水帘洞美猴王孙悟空"
message3 = """我是'花果山'水帘洞"美猴王"孙悟空"""
# 4.转义字符:改变含义的特殊字符
# \"  \'  \n换行   \\   r"原始字符"
message3 = "我是\"花果山\"水帘洞\"美猴王\"孙悟空"
message4 = "我是花果山水帘洞\n美猴王孙悟空"
url = "C:\\arogram\\bnternet\images"
url = r"C:\arogram\bnternet\images"
print(url)
# 5. 格式化字符串：在字符串中插入变量
# "格式"%(变量)
# 占位符:原样输出%s   保留小数精度%f   保留整数宽度%d
usd = 1.2
cny = usd * 6.6727
print(str(usd) + "美元=" + str(cny) + "人民币")
print("%s美元=%s人民币" % (usd, cny))

money = 1.23956789
print("金额是:%s" % money)
print("金额是:%.2f" % money)

# 04:05
hour = 4
minute = 5
print("%s:%s" % (hour, minute)) # 4:5
print("%.2d:%.2d" % (hour, minute)) # 4:5
