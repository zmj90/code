# xpath语句

html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>xpath</title>
    </head>
    <body>
        <ul>
            <li>第1</li>
            <li name='n2'>第2</li>
            <li>第21</li>
        </ul>
    </body>
</html>"""

from lxml import etree

eobject = etree.HTML(html)
# print(eobject)

print(eobject.xpath('//title/text()'))
print(eobject.xpath('//ul/li/text()'))

lis = eobject.xpath('//ul/li')

for li in lis:
    print(li.xpath('./text()'))

# 获取ul中的第2个li中文本数据
print(eobject.xpath('//ul/li[2]/text()'))

# 获取ul下的name属性为‘n2’的li节点下的文本 (<li name='n2'>文本</li>) --> '文本'
print(eobject.xpath('//ul/li[@name="n2"]/text()'))

# 获取ul下的name属性为‘n2’的li节点下name属性的值（<li name='n2'>） --> "n2"
print(eobject.xpath('//ul/li[@name="n2"]/@name'))