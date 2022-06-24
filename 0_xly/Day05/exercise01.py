from lxml import etree

html = '''<ul class="rank-list">
				<li class="current">
			        <em class='n1'>1</em>					<a href="/cell_phone/index1399155.shtml" class="pic" title="OPPO Find X5 Pro（12GB/512GB/5G版）" target="_blank">
				<img width="80" height="60" alt="OPPO Find X5 Pro（12GB/512GB/5G版）" src="https://i1-prosmall-fd.zol-img.com.cn/t_s80x60/g7/M00/0E/0F/ChMkLGIXiiOIDNL6AAGwTcvty5gAAA76wP5RqwAAbBl937.jpg">
			</a>
			<p><a title="OPPO Find X5 Pro（12GB/512GB/5G版）" href="/cell_phone/index1399155.shtml" target="_blank">OPPO Find X5 Pro（12GB/512..</a></p>
			<p><em class="price">￥6799</em></p>
					</li>
			</ul>'''

etr = etree.HTML(html)

# 排名  15:10 回来
num = etr.xpath('//ul/li/em/text()')
print(num)

# 名称
name =etr.xpath('//ul/li/a/@title')
print(name)