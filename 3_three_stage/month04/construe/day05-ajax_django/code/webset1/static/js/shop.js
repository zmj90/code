function shop(){
    // 1.get请求渲染页面:
    $.ajax({
        type:'get',
        url: 'http://127.0.0.1:8000/book/',
        datatype: JSON,
        success: function (response){
            var data_list = response.split('|')
            console.log(data_list[0].split('_'))
            html = ''
            for (var i=0;i<data_list.length;i++){
                data = data_list[i].split('_')
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
            $('#goods').html(html)
        }
       
       
        
        //     var html=''
        //     for (var i=0;i<data_list.length;i++){
        //         data = data_list[i].split('_')
        //         console.log(data)
        //     html += '<tr><td><table border="0"><tr><td><img width="100" height="100" src="'
        //     html += data[3]
        //     html += '"></td><td valign="top"><table border="0"><tr><td width="250"><font color="black">'
        //     html += data[1]
        //     html += '</font></td></tr> <tr valign="top"><td ><font color="#dc143c" size="5">惊爆价:￥'      
        //     html += data[2]
        //     html += '</font></td></tr><tr><td ><font color="black">书名:'
        //     html += data[0]
        //     html += '</font></td></tr>'
        //     html += '<tr><td ><font color="black">出版日期:'
        //     html += data[4]
        //     html += '</font></td></tr><table border="0"><tr><td bgcolor="#dc143c" align="center" width="80"><a href="" >Buy Now</a></td><td width="25"></td>'
        //     html += '<td bgcolor="#ffb6c1" width="80" align="center"><font color="#dc143c">add to cart</font></td></tr></table></td></tr></table></td></tr>'
        //     }
        // // 向某一标签添加html代码
        // $('#goods').html(html)
        // } 
    })
}

// 简述:页面加载完成,立即调用函数
window.onload = function () {
    shop()
}
