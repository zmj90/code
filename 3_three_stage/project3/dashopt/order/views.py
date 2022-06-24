import datetime

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from user.models import *
from utils.logging_dec import logging_check
from carts.views import CartsView
from django.conf import settings
import json
from order.models import OrderInfo, OrderGoods, SKU

# Create your views here.

class AdvanceViews(View):

    def get_address(self, user_id):
        all_address = Address.objects.filter(is_active=True, user_profile_id=user_id)
        default_address = []
        no_default_address = []

        for addr in all_address:
            addr_dict = {}
            addr_dict["id"] = addr.id
            addr_dict["name"] = addr.receiver
            addr_dict["mobile"] = addr.receiver_mobile
            addr_dict["title"] = addr.tag
            addr_dict["address"] = addr.address
            if addr.is_default:
                default_address.append(addr_dict)
            else:
                no_default_address.append(addr_dict)
        return default_address + no_default_address

    def get_order_carts_list(self, user_id):
        carts_obj = CartsView()
        sku_list = carts_obj.get_carts_list(user_id)

        return [s for s in sku_list if s["selected"] == 1]

    @logging_check
    def get(self, request, username):
        settlement_type = request.GET.get("settlement_type")

        if not settlement_type:
            return JsonResponse({"code": 10500, "error": "Please give me type"})

        settlement_type = int(settlement_type)

        # 地址数据
        user = request.myuser
        address_list = self.get_address(user.id)

        if settlement_type == 0:
            # 购物车
            sku_list = self.get_order_carts_list(user.id)
            # 购物车中选中商品数据

        else:
            # 直接购买
            sku_list = []

        data = {}
        data["addresses"] = address_list
        data["sku_list"] = sku_list

        return JsonResponse({"code": 200, "data": data, "base_url": settings.PIC_URL})


class OrderInfoView(View):

    def get_carts_order_data(self, uid):

        carts_obj = CartsView()
        # carts_1 - {'sku_id':[count, select]}
        all_data = carts_obj.get_carts_all_data(uid)
        return {k:v for k, v in all_data.items() if v[1] == 1}


    @logging_check
    def post(self, request, username):
        user = request.myuser
        json_str = request.body
        json_obj = json.loads(json_str)
        address_id = json_obj.get("address_id")
        # TODO
        # 直接购买进入， 则多出sku相关参数
        try:
            address = Address.objects.get(user_profile_id=user.id, id=address_id, is_active=True)
        except Exception as e:
            print(e)
            return JsonResponse({"code": 10501, "error": "The address is error"})
        # 插入订单
        # 订单商品数据
        # SKU数据 update
        with transaction.atomic():
            sid = transaction.savepoint()
            # 生成订单号
            now = datetime.datetime.now()
            order_id = "%s%02d"%(now.strftime("%Y%m%d%H%M%S"), user.id)
            total_amount = 0
            total_count = 0


            order = OrderInfo.objects.create(
                order_id=order_id,
                user_profile=user,
                address=address.address,
                receiver=address.receiver,
                receiver_mobile=address.receiver_mobile,
                tag=address.tag,
                tolal_amount=total_amount,
                total_count=total_count,
                freight=1,
                pay_method=1,
                status=1,
            )

            #取购物车数据
            carts_dict = self.get_carts_order_data(user.id)
            skus = SKU.objects.filter(id__in=carts_dict.keys())

            #检查库存、是否上架/ 修改库存 / 创建订单商品数据
            #删除购物车选中商品
            #transaction.savepoint_rollback(sid)
            for sku in skus:
                if not sku.is_launched:
                    continue




