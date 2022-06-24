import redis
import requests
from fake_useragent import UserAgent
import re
import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='mu7401889.', database='beike', charset='utf8')
cur = db.cursor()
url = 'https://cd.ke.com/ershoufang/pg1'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Cookie': ' select_city=510100; digv_extends=%7B%22utmTrackId%22%3A%2280419289%22%7D; lianjia_ssid=e094d850-b487-4d47-acd4-81ea0bffd6cf; lianjia_uuid=45136193-b230-44e4-8f34-c79757e6ea23; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1594776031; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1594776534; gr_user_id=f53afe52-818b-4ca6-909e-8f31271d1773; gr_session_id_a1a50f141657a94e=5f55d639-65e6-440b-a1bc-fc4775b1c455; gr_session_id_a1a50f141657a94e_5f55d639-65e6-440b-a1bc-fc4775b1c455=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22173500f0f66682-011363614f10318-4c302372-1327104-173500f0f678f%22%2C%22%24device_id%22%3A%22173500f0f66682-011363614f10318-4c302372-1327104-173500f0f678f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wychengdu%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; sajssdk_2015_cross_new_user=1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNDUwOTE1MWY5OGI2MjE2N2RkMmU4OGIxM2UzNTc0ODA3M2QxYjhkZTkzZWE2MWY4ODFjYjBmZjljZjUzMzEyOTc0ZDk5YWE1ZjdiMTMzNTZhMzY0YmU0ZTZmNTJmYTFmNTU0M2Y3MDExYWE3MjM5YjA4MzQzNzE5MTZhMWM5YTU3N2ZjNDk4NTQ5NzQwZmRkMTJhYzM4NjI4NjYzMjFhMDBiMzEzYzIyNWU5NDM1ODFkZjk0ZDM2MDViNjVhYzM1MGZkOWRhYjQ0Yzg4ODk5MDEzYTZjODAzNDk4NTM0NDlhNTEyMjRiNjVjZGJjMDg5YWFiNTlmODU1MTM1NDAxMTg3MTBiZDg2MDE0ZDYxYzYyZGUzYmVmMzkzOTExNDJiYzAzM2FmN2I4ZWZhYTFjODYwNGE4ODk0ODU4YTVmNjdjMmY2Mjg1NzUzMGRiMDQxMDY1YTBlZjU5YmI2NzY2Y1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5MTIyZWIxMFwifSIsInIiOiJodHRwczovL2NkLmtlLmNvbS9lcnNob3VmYW5nL3BnMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
    'Host': 'cd.ke.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': UserAgent().random,
}
html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')

data = re.findall(r'<li class="clear">.*?</li>', html, re.S)
sql = 'insert into beike.beike values (%s,%s,%s,%s,%s,%s,%s,%s)'
for home in data:
    # print(home)
    # break
    message = re.findall(
        r'<div class="address">.*?<a.*?>(.*?)</a>.*?<span class="houseIcon">.*?</span>(.*?)</div>.*?<div class="totalPrice"><span>(.*?)</span>.*?<div class="unitPrice".*?<span>(.*?)</span>',
        home, re.S)
    data1 = [s1.strip() for s1 in message[0][1].split('|')]
    print(data1)
    count, year, layout, area, orientation = data1
    name, price, unit_price = message[0][0], message[0][2], message[0][3]
    try:
        cur.execute(sql,args=(name,count, year, layout, area, orientation, price, unit_price))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
