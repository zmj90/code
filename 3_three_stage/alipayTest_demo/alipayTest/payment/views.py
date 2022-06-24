import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from alipay import AliPay
from django.conf import settings

app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()

alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()

ORDER_STATUS = 0  #０代表未付款，　１已付款　

class MyAliPay(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #初始化alipay
        self.alipay = AliPay(
            appid= settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string= app_private_key_string,
            alipay_public_key_string= alipay_public_key_string,
            sign_type='RSA2',
            debug=True #debug模式，请求转发到沙箱模式
        )

    def get_trade_url(self, order_id, amount):
        #生成支付宝支付链接

        #https://openapi.alipaydev.com/gateway.do? + 查询字符串
        query_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no= order_id,
            total_amount= amount,
            subject=order_id,
            return_url= settings.ALIPAY_RETURN_URL,
            notify_url= settings.ALIPAY_NOTIFY_URL
        )
        return "https://openapi.alipaydev.com/gateway.do?" + query_string

    def get_verify_result(self, data, sign):
        #调用支付宝验签，成功返回True False则失败
        return self.alipay.verify(data, sign)


    def get_trade_result(self, order_id):

        #查询支付结果
        result = self.alipay.api_alipay_trade_query(order_id)
        print('---query result is')
        print(result)
        if result.get('trade_status') == 'TRADE_SUCCESS':
            return True
        return False



class JumpView(MyAliPay):

    def get(self, request):

        return render(request, 'ajax_alipay.html')

    def post(self, request):
        #获取支付地址
        json_obj = json.loads(request.body)
        order_id = json_obj['order_id']
        return JsonResponse({'pay_url':self.get_trade_url(order_id,999)})



class ResultView(MyAliPay):

    #重定向操作
    def get(self, request):

        request_data = {k:request.GET[k] for k in request.GET.keys()}
        print('request_data GET')
        print(request_data)
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)
        if is_verify is True:
            #验签成功
            order_id = request_data.get('out_trade_no')
            if ORDER_STATUS == 1:
                # 被动接受
                return HttpResponse('订单支付成功')

            else:
                #主动查询
                result = self.get_trade_result(order_id)
                if result:
                    print('更改订单状态')
                    #ORDER_STATUS = 1
                    return HttpResponse('主动查询订单支付完成')
                else:
                    return HttpResponse('支付失败')

        else:
            return HttpResponse('违法访问')



    def post(self, request):

        #表单数据取出来，验签
        #校验成功后，　request_data, trade_status
        #根据交易状态　修改订单状态
        pass
