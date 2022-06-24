'''
需求：
    1、获取一级页面：手机列表页面
        拿到：进入二级页面的URL
    2、向二级页面的URL发送请求
        数据：手机名称
             报价
             总和评分+5项评分
             内存
             电池
             屏幕
    3、保存数据到CSV文件
    4、数据分析
'''
import requests
from lxml import etree

#  一级页面的URL地址
first_url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html'

# 伪装的请求头
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


def get_html(url):
    '''
        通过URL获取页面数据
    :param url: 请求的URL地址
    :return: 获取的页面数据（str）
    '''
    resp = requests.get(url, headers=header)
    return resp.text


def get_next_html_link(html):
    '''
        解析一级页面中的二级页面链接
    :param html: 一级页面网页源代码
    :return:
    '''
    ele = etree.HTML(html)

    # 二级页面链接
    two_link = ele.xpath('//ul[@id="J_PicMode"]/li/a/@href')
    # print(two_link)

    # 构建完整二级页面链接(48个)
    list_two_link = []
    for link in two_link:
        two_url = 'https://detail.zol.com.cn' + link
        list_two_link.append(two_url)

    return list_two_link


def parse_two_html(html):
    '''
        解析二级页面
    :param html: 二级页面源代码
    :return:
    '''

    ele = etree.HTML(html)

    # 手机名称
    name = ele.xpath('//h1/text()')[0].split('（')[0]

    # 手机价格
    price = ele.xpath('//b[@class="price-type"]/text()')

    # 评分
    # 包含所有分数的div
    score_div = ele.xpath('//div[@class="review-comments-score clearfix"]')[0]

    try:
        score0 = score_div.xpath('./div[1]/strong/text()')
        score1 = score_div.xpath('./div[2]/div[1]//div[@class="circle-value"]/text()')
        score2 = score_div.xpath('./div[2]/div[2]//div[@class="circle-value"]/text()')
        score3 = score_div.xpath('./div[2]/div[3]//div[@class="circle-value"]/text()')
        score4 = score_div.xpath('./div[2]/div[4]//div[@class="circle-value"]/text()')
        score5 = score_div.xpath('./div[2]/div[5]//div[@class="circle-value"]/text()')
    except:
        score0 = 0
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0

        # 内存
    saving = ele.xpath('//div[@class="info-list-01"]/ul/li[4]/div/a[@class="product-link"]/text()')

    # 电池
    electr = ele.xpath('//div[@class="info-list-01"]/ul/li[5]/div[1]/span[1]/text()')

    print([name, price, score0, score1, score2, score3, score4, score5, saving, electr])


# 1 获取一级页面中的网页数据
one_html = get_html(first_url)

# 2 从一级页面中解析出二级页面的链接
list_two_link = get_next_html_link(one_html)
# print(list_two_link, len(list_two_link))

# 3 向二级页面发送请求，获取页面数据
for url in list_two_link[1:2]:
    print('二级页面链接:', url)

    # 获取二级页面数据
    two_html = get_html(url)
    # print(two_html)

    # 解析二级页面
    parse_two_html(two_html)
