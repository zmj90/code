# AJAX知识点复盘

## 1.AJAX动态渲染页面

### 1.1获取图书信息渲染到页面:

页面的数据:

静态数据		----    写好的页面       （货架)

动态数据        ----    后端提供的数据  (商品)

![](images\UI图.png)

### 1.2:分析页面需要动态渲染的标签:

- 分析页面标签结构
- 分析页面动态数据的位置

```html
<table align="center" border="0" id="goods">
    <tr>
      <td>
        <table border="0">
          <tr>
            <td><img src="/static/images/Lipstick.webp"></td>
            <td valign="top">
              <table border="0">
                <tr>
                  <td width="250"><font color="black">Girl, you're going to be a woman</font></td>
                </tr>
                <tr valign="top">
                  <td ><font color="#dc143c" size="5">$16</font></td>
                </tr>
                <tr>
                  <td ><font color="black">Lipstick</font></td>
                </tr>
                <tr>
                  <td ><font color="black">生产日期:xx/xx/xx</font></td>
                </tr>
              </table>
              <table border="0">
                <tr>
                  <td bgcolor="#dc143c" align="center" width="80"><a href="" >Buy Now</a></td>
                  <td width="25"></td>
                  <td bgcolor="#ffb6c1" width="80" align="center"><font color="#dc143c">add to cart</font></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
</table>
```

- 1.通过页面分析得到结果 页面展示的数据都在 表格标签#goods下的tr标签中，且通过tr标签的重复展示出网页内的数据

- 2.页面中包含的数据有 describe-商品描述,title-商品名字,picture-商品图片,price-商品价格,publisher_date-出版日期.

- 后端数据量多少个(五种动态数据)，前端渲染多少本的图书信息

- 前端渲染多少本图书的信息，页面就写多少个tr标签.

-  前端需求的数据结构

    [(书名1,描述1,单价1,出版日期1,图片1)，(书名2,描述2,单价2,出版日期2,图片2)]

- for x in list:

  ​       x[0]

- django能够满足的数据结构

  ```python
  datas='书名1_描述1_单价1_出版日期1_图片1|书名2_描述2_单价2_出版日期2_图片2'
  data_list = datas.split('|')
  datas = ['书名1_描述1_单价1_出版日期1_图片1'，'书名2_描述2_单价2_出版日期2_图片2']
  data = datas[0] # '书名1_描述1_单价1_出版日期1_图片1'
  data = data.split('_') # [书名1,描述1,单价1,出版日期1,图片1]
  ```

  

### 1.3后端组织数据

- 后端组织相应数据结构交给前端渲染

```python
def get_data(request):
    if request.method == "GET":
        # #1.示意 基本查詢 all()
        books = Book.objects.all()
        datas = ''
        for book in books:
            data = "%s_%s_%s_%s_%s"%(book.title,book.describe,str(book.price),'http://127.0.0.1:8000/media/' + str(book.picture),str(book.publisher_date))
            datas += data
            datas += '|'
        datas = datas[0:-1]
    return HttpResponse(datas)
```

### 1.4AJAX请求获取数据

- ajax动态渲染页面:

```javascript
function shop(){
   $.ajax({
        type:'get',
        url: 'http://127.0.0.1:8000/book/',
        datatype: JSON,
        success: function (response){
            console.log(response)
            var data_list = response.split('|')
            var html=''
            for (var i=0;i<data_list.length;i++){
                data = data_list[i].split('_')
                console.log(data)
            html += '<tr><td><table border="0"><tr><td><img width="100" height="100" src="'
            html += data[3]
            html += '"></td><td valign="top"><table border="0"><tr><td width="250"><font color="black">'
            html += data[1]
            html += '</font></td></tr> <tr valign="top"><td ><font color="#dc143c" size="5">惊爆价:￥'      
            html += data[2]
            html += '</font></td></tr><tr><td ><font color="black">书名:'
            html += data[0]
            html += '</font></td></tr>'
            html += '<tr><td ><font color="black">出版日期:'
            html += data[4]
            html += '</font></td></tr><table border="0"><tr><td bgcolor="#dc143c" align="center" width="80"><a href="" >Buy Now</a></td><td width="25"></td>'
            html += '<td bgcolor="#ffb6c1" width="80" align="center"><font color="#dc143c">add to cart</font></td></tr></table></td></tr></table></td></tr>'
            }
        // 向某一标签添加html代码
        $('#goods').html(html)
        } 
    })
}
// 页面加载完成，调用shop()进行动态数据渲染
window.onload = function () {
    shop()
}
```
