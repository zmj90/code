"""
    多线程抓取链家二手房数据
"""
import json
import requests, random, time
from threading import Thread, Lock
from queue import Queue
from fake_useragent import UserAgent
from lxml import etree


class SecHouse:
    def __init__(self):
        self.url = 'https://cd.lianjia.com/ershoufang/pg{}/'
        self.headers = {'User-Agent': UserAgent().random}
        self.queue = Queue()
        self.lock = Lock()

    def get_html(self):
        while True:
            self.lock.acquire()
            if not self.queue.empty():
                url = self.queue.get()
                self.lock.release()
                html = requests.get(url=url, headers=self.headers).content.decode('utf-8', 'ignore')
                self.parse_html(html)
            else:
                self.lock.release()
                break

    def parse_html(self, html):
        parse = etree.HTML(html)
        house_list = parse.xpath('//ul[@class="sellListContent"]/li')
        for house in house_list:
            house_info = {}
            name_list = house.xpath('//div[@class="title"]/a/text()')
            house_info['title'] = name_list[0] if name_list else None
            address1_list = house.xpath('//div[@class="positionInfo"]/a[1]/text()')
            address2_list = house.xpath('//div[@class="positionInfo"]/a[2]/text()')
            house_info['address'] = address1_list[0] + '-' + address2_list[0] if address1_list or address2_list else None
            type_list = house.xpath('//div[@class="houseInfo"]/text()')
            house_info['type'] = type_list[0] if type_list else None
            follow_list = house.xpath('//div[@class="followInfo"]/text()')
            house_info['followInfo'] = follow_list[0] if follow_list else None
            price_list = house.xpath('//div[@class="totalPrice"]/span/text()')
            house_info['total_price'] = price_list[0] if price_list else None
            unit_price_list = house.xpath('//div[@class="unitPrice"]/span/text()')
            house_info['unit_price'] = unit_price_list[0] if unit_price_list else None
            print(house_info)

    def url_in_queue(self):
        for i in range(1, 101):
            url = self.url.format(i)
            self.queue.put(url)

    def run(self):
        self.url_in_queue()
        t_list = []
        for i in range(5):
            t = Thread(target=self.get_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()


if __name__ == '__main__':
    spider = SecHouse()
    spider.run()
