
function rand(min,max) {
    return Math.floor(Math.random()*(max-min))+min;
}

//模拟数据 向后端传订单id
var random_id = rand(1000,9999)
var order_id = "2019111821315602" + random_id.toString()
post_data = {"order_id": order_id}
console.log(post_data)

$(function(){
    $("#Btn_pay").click(function () {
        $.ajax({
            url:"http://127.0.0.1:8000/payment/jump/",
            type:"post",
            contentType: "application/json",
            dataType:"json",
            data: JSON.stringify(post_data),
            success:function (data) {
                window.location = data.pay_url
            },
            error:function(errors){
                console.log("错误")
                console.log(errors)
            }
        })
    })
})
