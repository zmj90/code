"""
    二维列表
    	列表名[行索引][列索引]
"""
list01 = [
      [1, 2, 3, 4, 5],
  	  [6, 7, 8, 9, 10],
 	  [11, 12, 13, 14, 15],
]
print(list01[0][0])
print(list01[0][3])
print(list01[2][1])

# print(list01[0][0])
# print(list01[0][1])
# print(list01[0][2])
# print(list01[0][3])
# print(list01[0][4])
# for c in range(5):
for c in range(len(list01[0])):
	print(list01[0][c])
