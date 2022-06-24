"""
买家账号eswxur0782@sandbox.com
登录密码111111
支付密码111111
用户名称沙箱环境
证件类型身份证(IDENTITY_CARD)
证件号码574655194603075214
账户余额
99999.00充值取现

商家账号uemtqb9713@sandbox.com
商户UID2088102180586944
登录密码111111
账户余额
0.00充值取现
"""

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from alipay import AliPay
from django.conf import settings
import json
# Create your views here.


app_private_key_string = open(settings.ALIPAY_KEY_DIRS + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIRS + 'alipay_public_key.pem').read()

ORDER_STATUS = 0  #０代表未付款，　１已付款

class MyAliPay(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 初始化alipay
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA2",
            debug=True # debug模式， 请求转发到沙箱模式
        )

    def get_trade_url(self, order_id, amount):
        # 生成支付宝支付链接
        # https: // openapi.alipaydev.com / gateway.do? + 查询字符串
        query_string = self.alipay.api_alipay_trade_page_pay(
            subject=order_id,
            out_trade_no=order_id,
            total_amount=amount,
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_NOTIFY_URL
        )
        return "https://openapi.alipaydev.com/gateway.do?" + query_string

    def get_verify_result(self, data, sign):
        # 调用支付宝签名, 成功True,失败False
        return self.alipay.verify(data, sign)

    def get_trade_result(self, order_id):
        # 查询支付结果
        result = self.alipay.api_alipay_trade_query(order_id)
        print('---query result is')
        print(result)
        if result.get('trade_status') == 'TRADE_SUCCESS':
            return True
        return False


class JumpView(MyAliPay):

    def get(self,request):
        return render(request, 'ajax_alipay.html')

    def post(self, request):
        # 获取支付地址
        json_obj = json.loads(request.body)
        order_id = json_obj['order_id']
        return JsonResponse({'pay_url': self.get_trade_url(order_id, 999)})


class ResultView(MyAliPay):

    # 重定向操作
    def get(self, request):
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        print(request_data)
        sign = request_data.pop('sign')
        is_verify = self.get_verify_result(request_data, sign)
        if is_verify:
            # 验签成功
            order_id = request_data.get('out_trade_no')
            if ORDER_STATUS == 1:
                return HttpResponse('订单支付成功')
            else:
                # 主动查询
                result = self.get_trade_result(order_id)
                if result:
                    print('更改订单状态')
                    return HttpResponse('主动查询订单支付完成')
                else:
                    return HttpResponse('支付失败')
        else:
            return HttpResponse('违法访问')