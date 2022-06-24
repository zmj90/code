# **现有lists = ['C', 'Python', 'Java', 'C++']**

lists = ['C', 'Python', 'Java', 'C++']
# **1、向列表中添加：C#, PHP**
lists.append('C#')
lists.append('PHP')
print(lists)

# **2、查看排名第2、第3位的编程语言**
print(lists[1], lists[2])
print(lists[1:3])

# **3、修改：第4名的编程语言为：SQL**
lists[-3] = "SQL"
print(lists)

# **4、删除第5、第6的编程语言**
del lists[-1]
del lists[-1]

# del lists[-2:]
print(lists)

# **5、按降序排列，每一行打印一门语言**
lists.sort(reverse=True)
print(lists)

# for lang in lists:
#     print(lang)


for i in range(len(lists)):
    print('排名第{}：{}'.format(i+1, lists[i]))