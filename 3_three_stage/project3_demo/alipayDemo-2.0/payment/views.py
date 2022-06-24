from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from alipay import AliPay
from django import http
import json
import copy
from django.conf import settings

# Create your views here.
# 本demo未配置数据库故订单id等使用常量表示
TOTAL_AMOUNT = 159            # 订单金额[此金额需要后端通过数据查询]
ORDER_STATUS = 0              # 订单状态 0 初始状态  1 未付款  2 已付款 

app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()

class MyAliPay(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,  # 默认回调url-　阿里与商户后台交互
            # 使用的文件读取方式,载入支付秘钥
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            # 使用文件读取的方式,载入支付宝公钥
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False  True则将转发沙箱环境
        )


    def get_trade_url(self, order_id, amount):
        #生成支付地址链接
        # 电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string
        # 测试方式此为支付宝沙箱环境
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount= amount,
            subject=order_id,
            # 回转url,　支付宝与买家业务处理完毕(支付成功)将玩家重定向到此路由,带着交易的参数返回
            return_url= settings.ALIPAY_RETURN_URL,
            notify_url= settings.ALIPAY_NOTIFY_URL  # 可选, 不填则使用默认notify url
        )
        return "https://openapi.alipaydev.com/gateway.do?" + order_string

    def get_trade_result(self, order_id):
        #查询支付结果
        result = self.alipay.api_alipay_trade_query(out_trade_no=order_id)  # 主动查询接口
        if result.get("trade_status", "") == "TRADE_SUCCESS":
            return True
        return False

    def get_verify_result(self, data, sign):
        #验证签名 - True 成功 False 失败
        return self.alipay.verify(data, sign)


# 处理跳转支付宝业务
class OrderProcessingnView(MyAliPay):
    # 获取跳转支付页面
    def get(self,request):
        return render(request,'ajax_alipay.html')
    # 确认支付获取支付宝支付URL
    def post(self,request):
        json_obj = json.loads(request.body)
        #前端将订单号传至后端
        order_id = json_obj.get('order_id')
        return http.JsonResponse({"status":1,"pay_url":self.get_trade_url(order_id,TOTAL_AMOUNT)})

# 处理支付宝回调及重定向业务
class PaymentResultView(MyAliPay):

    # 重定向接口
    def get(self, request):
        # 1.获取参数字典,验签结果,alipay对象
        request_data = {k:request.GET[k] for k in request.GET.keys()}
        print('request_data GET')
        print(request_data)
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)
        # 2.根据验证结果进行业务处理
        if is_verify is True:
            order_id = request_data.get('out_trade_no', None)
            if ORDER_STATUS == 2:
                return HttpResponse("订单支付成功")
            # 主动查询
            else:
                result = self.get_trade_result(order_id) #  主动查询接口
                if result:
                    print('更改订单状态')
                    #ORDER_STATUS = 2
                    return HttpResponse("主动查询结果订单支付完成了")
                else:
                    return HttpResponse("支付未完成")
        else:
            return HttpResponse("非法访问")

    # 回调接口
    def post(self, request):
        """
        处理支付宝的付款回调业务
        :param request:
        :return:
        """
        # 1.获取参数字典,验签结果,alipay对象
        request_data = {k:request.POST[k] for k in request.POST.keys()}
        print('request_data POST')
        print(request_data)
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)
        # 2.根据验证结果进行业务处理
        if is_verify is True:
            trade_status = request_data.get('trade_status', None)
            if trade_status == "TRADE_SUCCESS":
                print('更改订单状态')
                #ORDER_STATUS = 2
                return HttpResponse("success")
        else:
            return HttpResponse("非法访问")
