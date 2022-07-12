"""
    Python语言有哪些数据类型
        可变类型:预留空间+自动扩容
            例如:list...
            优点:存储数据更加方便(支持增删改)
            缺点:占用内存较多

        不可变类型:按需分配
            例如:int/float/bool/str/tuple...
            优点:占用内存较少
            缺点:存储数据不方便(创建后必须确定数据)
            适用性:优先
    元组基本操作
        创建
        定位(只读)
        遍历
"""
# 1. 创建
# -- 根据元素:元组名 = (数据1,数据2)
tuple_name = ("樊威虎", "李杨", "彭文韬")
# -- 根据元素:元组名 =  tuple(可迭代对象)
list_name = ["樊威虎", "李杨", "彭文韬"]  # 存储计算过程中的数据
tuple_new = tuple(list_name)  # 存储计算的结果

# 2. 定位
# -- 索引
print(tuple_name[-2])  # 倒数第二个
# -- 切片
print(tuple_name[-2:])  # 最后两个

# 3. 遍历
# -- 从头到尾读取
for item in tuple_name:
    print(item)

# -- 非从头到尾读取
for i in range(len(tuple_name) - 1, -1, -1):
    print(tuple_name[i])

# 注意1:在没有歧义的情况下,构建元组可以省略小括号
tuple_name = "樊威虎", "李杨", "彭文韬"
# 特别要小心:创建数据时,容易写成元组
# name = "悟空",

# 注意2:如果元组只有一个元素,必须添加逗号
tuple01 = (10,)
print(type(tuple01))

# 注意3:序列拆包
a,b,c = tuple_name
a,b,c = list_name
a,b,c = "樊威虎"
print(a)
print(b)
print(c)

# 变量交换
a = 1
b = 2
a,b = b,a

