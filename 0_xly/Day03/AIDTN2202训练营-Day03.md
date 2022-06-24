# AIDTN2202训练营-Day03

## 1、课程回顾

1 while 循环语句

- 作用：根据条件重复执行某些语句
- 语法
    
    ```python
    while 条件:
        循环体
    else:
        语句
    ```

- while死循环

  ```Python
  while True:
      循环体
  ```

- break语句

  - 功能：结束当前循环
  - 说明：
    - 1、break之后的语句不执行
    - 2、break只能使用在循环中
    - 3、如果while中执行了break语句，则else不执行。

- 2 for 循环语句

  - 功能：用于遍历可迭代对象中的数据。

  - 语法：

    ```python
    for 变量 in 可迭代对象：
    	循环体
    else:
        语句
        
    快捷输入：iter + Enter
    ```

- 总结

  - while：用于条件会改变、死循环
  - for：用于有限循环次数

3、字符串

	- 功能：用于描述文本信息。
	- 表示方式：' '   " "   ''' '''    """ """
	- 运算：+   +=    \*   \*=
 - 索引：str[index]
   	- index：索引值，正向从0开始，反向从-1开始
   	- 注意：索引值越界
- 切片：str[[start]:[stop]\[:step]]
  - 注意：获取为空（''）
    - 1、步长方向与start-stop的方向相反。
    - 2、start-stop重合。

- 方法
  - str.replace(old, new, count=-1)  替换
  - str.strip(char)  去除指定字符



## 2、字符串 - str

- 格式化：
  - ‘{} {} ...’.format(数据1, 数据2, ...)

## 3、列表 - list

- 功能：存储任意类型的数据。
- 表示：[数据1, 数据2, ...]
- 操作：
  - 创建
    - 空：变量名 = []
    - 非空：list(可迭代对象)
  - 增加
    - list.append(元素)
  - 删除
    - del list[索引值]
  - 修改
    - list[索引值] = 值
  - 查看
    - 长度：len(list)
    - 索引：list[索引值]
    - 切片：list[start:stop:step]
    - 存在：元素 in/not in list
  - 排序
    - list.sort(reverse=False)   升序
      - reverse=True  降序
  - 遍历
    - 方法1：直接遍历元素
      - for 变量 in list:
        - 循环体
    - 方法2：遍历列表的长度【对应的是索引值】
      - for 变量 in range(len(list)):
        - 循环体

----

**现有lists = ['C', 'Python', 'Java', 'C++']**

**1、向列表中添加：C#, PHP**

**2、查看排名第2、第3位的编程语言**

**3、修改：第4名的编程语言为：SQL**

**4、删除第5、第6的编程语言**

**5、按降序排列，每一行打印一门语言**

---

- 与字符串的互操作
  - list --> str
    - '连接字符'.join(list)
      - 注意：list中的元素必须是字符串类型
  - str --> list
    - str.split(字符, 个数)
      - 默认是按照任意个空白分割

---

练习1：猜拳小游戏

电脑随机出：石头、剪刀、布，用户也是输入：石头剪刀布，每次打印：电脑出：xxx，用户出：xxx, xxx赢了，最终打印：电脑与用户各赢多少局。

练习2：彩票生成器

产生一注双色球并打印。

红色：取值 [1, 33]

蓝色：取值 [1, 16]

规则：

​	1、一共是7个球（6红1蓝）

​	2、6个红色的数字不能相同



## 4、字典 - dict

- 功能：用于【键值对】的数据容器。
- 表示：{键1:值1, 键2:值2, 键3:值3, ...}
- 作用：描述一一对应关系的数据。
- 操作：
  - 创建
    - 空：变量名 = {}
  - 查看
    - 长度：len(dict)
    - 取key对应的值：dict[key]
    - key是否存在: key not in/in dict
  - 增加/修改
    - dict[key] = 值
      - 增加：key不存在
      - 修改：key存在     
  - 删除
    - del dict[key]
  - 遍历
    - 方式1：直接遍历键值对
      - for 变量 in dict:   # 变量接受的key
        - 循环体
    - 方式2：直接获取key与value
      - 变量1接受的是key, 变量2接受的是value
      - for 变量1, 变量2 in dict.items():
        - 循环体