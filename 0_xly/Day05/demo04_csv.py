import csv

# 打开文件，获取文件对象
file_obj = open('python.csv', 'w')

# 获取csv写入对象
writer = csv.writer(file_obj)

# 一行行写入数据
writer.writerow(['名称', '价格'])
# writer.writerow(['P50', 6599])
# writer.writerow(['mate50', 7599])

# 一次写入多个数据
data = [['P50', 6599],
        ['mate50', 7599]]
writer.writerows(data)

# 关闭文件
file_obj.close()
