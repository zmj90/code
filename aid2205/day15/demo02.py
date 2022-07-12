"""
    迭代 iteration
        每一次重复得到的结果将作为下一次重复的开始(过程)
    迭代器对象 iterator
        完成迭代过程的对象,具有__next__函数
    可迭代对象 iterable
        创建迭代器的对象,具有__iter__函数
"""
message = "我爱Python编程"
for item in message:
    print(item)

# for循环原理
# 1. 获取迭代器对象
iterator = message.__iter__()
# 2. 获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
    #3. 如果停止迭代退出循环
    except StopIteration:
       break

# 面试题:
# 对象能够参与for循环的条件是什么?
# 答：具有__iter__函数
