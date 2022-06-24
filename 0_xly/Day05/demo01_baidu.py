# 0 导包
import requests

# 1 确定URL地址
url = 'https://www.baidu.com'

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}

# 2 发送请求，获取响应对象
resp = requests.get(url, headers=header)

# 修改响应对象的编码方式
resp.encoding = 'gbk2312'

# 3 获取页面数据（页面源代码）
html = resp.text
print(html)