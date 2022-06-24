# file 文件

# # 操作1：读取文件数据
# # 1 打开文件
# file_obj = open('../Day03/read_file.py', 'r')
#
# # 2 读取数据   16:49 回来
# # data 接收的是读取的【字符串】数据
# # read 一次性读取所有内容
# data = file_obj.read()
# print(data, type(data))
#
# # 3 关闭文件
# file_obj.close()



# # 操作2：向文件中写入数据
# # 1 打开文件
# # 文件不存在则创建文件写入数据
# # 文件存在则会覆盖文件中的数据
# file_obj = open('read_file.txt', 'w')
#
# # 2 读取数据
# # 操作：最后存储数据
# text = '这是测试文件的写操作'
# data = file_obj.write(text)
# print(data)
#
# # 3 关闭文件
# file_obj.close()


# # 操作3：向文件中追加数据
# # 1 打开文件
# # 文件不存在/存在则创建文件追加数据
# file_obj = open('read_file2.txt', 'a')
#
# # 2 读取数据
# # 操作：最后存储数据
# text = '\n这是测试文件的追加操作3'
# file_obj.write(text)
#
# # 3 关闭文件
# file_obj.close()


# 操作3：向文件中追加数据
# 1 打开文件
# 文件不存在/存在则创建文件追加数据
file_obj = open('read_file2.txt', 'a')

# 2 读取数据
# 操作：最后存储数据
list_data = ['北京市', '东城区', '珍贝大厦']
string = '\n' + '-'.join(list_data)
file_obj.write(string)

# 3 关闭文件
file_obj.close()