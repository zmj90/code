window.onload = function (){
    // 获取 子服务器ID
    var app_server_id = $('#app_server_id').val()
    // 获取token
    var sso_token = localStorage.getItem('sso_token')
    // 根据子服务器ID生成 子服务器url
    if(app_server_id == '1'){
        location_url = 'http://127.0.0.1:8001'
    }if(app_server_id == '2'){
        location_url = 'http://127.0.0.1:8002'
    }
    // 如果token存在,证明用户使用过sso认证.
    if(sso_token){
        alert('用户已登录,点击确定跳转')
        window.location = location_url+'/user/verif/?sso_token='+sso_token
    }else{
        // 反之页面渲染出用户名密码的输入框
        html = ' <tr><td>username:  </td><td><input type="text" name="" id="username"> </td></tr><tr><td>password:  </td><td><input type="text" name="" id="password"></td></tr><tr><td><button id="go_login">登录</button></td></tr>'
        $('#login_body').html(html)
    }
    // 用户点击登录按钮,将数据提交到服务器.
    $('#go_login').click(function () {
            var username = $('#username').val()
            var password = $('#password').val()
            $.ajax({
                url:'http://127.0.0.1:8000/user/login/',
                type: 'post',
                datatype: 'json',
                contentType: "application/json;charset=utf-8",
                data: JSON.stringify({
                    'username':username,
                    'password':password
                }),
                success: function (response) {
                    // 将token存储到 localstorage（sso服务器域内)
                    var sso_token = response.data.token
                    var username = response.username
                    localStorage.setItem('sso_token',sso_token)
                    localStorage.setItem('username',username)
                    // 带着token跳转到对应的子服务器
                    window.location = location_url+'/user/verif/?sso_token='+sso_token
                }
            })
})
}