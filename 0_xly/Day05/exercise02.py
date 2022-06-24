from lxml import etree

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li name="n1">
            <a href="https://www.baidu.com">第1</a>
        </li>
        <li name="n2">
            <a href="https://www.danei.com">第2</a>
        </li>
        <li name="n3">
            <a href="https://www.tmooc.com">第3</a>
        </li>
    </ul>
</body>
</html>'''

# 获取etree对象
ele = etree.HTML(html)

# xpath语法
# '按字段获取'
# # name值
# name_res = ele.xpath('//ul/li/@name')
# print(name_res)
#
# # herf值
# href_res = ele.xpath('//li/a/@href')
# print(href_res)
#
# # a节点中的文本
# a_res = ele.xpath('//a/text()')
# print(a_res)


# '按记录获取'

lis = ele.xpath('//ul/li')
# print(lis)

for li in lis:
    # 从结果【列表】中获取第1个元素（0代表索引值）
    name = li.xpath('./@name')[0]
    href = li.xpath('./a/@href')[0]
    text = li.xpath('./a/text()')[0]
    print(name, href, text)