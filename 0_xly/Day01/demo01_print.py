# print函数使用介绍

# print(数据, ..., sep=' ', end='\n')
# 功能：打印数据
# 参数：
#    1 sep: 分隔符，默认是空格
#    2 end: 结束符，默认换行

# sep默认是空格
print('hello','python')
# 设置 sep 为 '-->'
print('hello','python',sep='-->')

# end='\n'  换行
# 不换行： 设置end='==='
print('hello','python',end='===')
print('<---->')

# sep='-', end='!!!'
print('您好，世界', 123, sep='-', end='!!!')