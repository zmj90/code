import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from goods.models import SKU
from utils.logging_dec import logging_check
from django.core.cache import caches
from django.conf import settings

CARTS_CACHE = caches['carts']


class CartsView(View):

    @logging_check
    def dispatch(self, request, *args, **kwargs):
        #分发方法
        #所有对应该视图类的请求，优先走该方法
        #集中检查  -  logging_check
        #集中处理参数 - json_obj
        json_str = request.body
        request.json_obj = {}
        if json_str:
            json_obj = json.loads(json_str)
            request.json_obj = json_obj

        return super().dispatch(request, *args, **kwargs)




    def get_cache_key(self, uid):

        return 'carts_%s'%(uid)


    def get_carts_all_data(self, uid):
        #获取用户购物车数据
        #carts_1 - {'sku_id':[count, select]}
        key = self.get_cache_key(uid)
        data = CARTS_CACHE.get(key)
        if not data:
            return {}
        return data

    def set_carts_data(self, uid, sku_id, info):
        #存储用户 指定sku_id的 购物车数据
        key = self.get_cache_key(uid)
        all_data = self.get_carts_all_data(uid)
        all_data[sku_id] = info
        CARTS_CACHE.set(key, all_data)

    def get_carts_list(self, uid):

        carts_data = self.get_carts_all_data(uid)
        if not carts_data:
            return []

        skus = SKU.objects.filter(id__in=carts_data.keys())
        skus_list = []

        # 按照前端要求 组织 返回数据
        for sku in skus:
            sku_dict = {}
            sku_dict['id'] = sku.id
            sku_dict['name'] = sku.name
            sku_dict['count'] = carts_data[sku.id][0]
            sku_dict['selected'] = carts_data[sku.id][1]
            sku_dict['price'] = str(sku.price)
            sku_dict['default_image_url'] = str(sku.default_image_url)
            sku_sale_attr_name = []
            sku_sale_attr_val = []
            # sku正向查询 查询出对应的 attr_val
            sale_attr_values = sku.sale_attr_value.all()
            for attr_value in sale_attr_values:
                sku_sale_attr_val.append(attr_value.name)
                # 销售属性值 正向查询 销售属性名
                sku_sale_attr_name.append(attr_value.spu_sale_attr.name)
            sku_dict['sku_sale_attr_name'] = sku_sale_attr_name
            sku_dict['sku_sale_attr_val'] = sku_sale_attr_val

            skus_list.append(sku_dict)

        return skus_list




    def post(self, request, username):

        json_obj = request.json_obj
        sku_id = json_obj['sku_id']
        count = json_obj['count']

        #检查sku
        try:
            sku = SKU.objects.get(id=sku_id, is_launched=True)
        except Exception as e:
            print('--sku error-- %s'%(e))
            return JsonResponse({'code':10400, 'error': 'The sku is error'})

        count = int(count)
        if count > sku.stock:
            return JsonResponse({'code':10401, 'error':'The count is error'})

        #获取购物车数据
        user = request.myuser
        carts = self.get_carts_all_data(user.id)
        #{'sku_id':[], 'sku_id2':[]....}
        if not carts:
        #    第一次使用购物车
            my_sku_info = [count, 1]
        else:
        #     #检查购物车数据里 有没有当前商品
            my_sku_info = carts.get(sku.id)
            if not my_sku_info:
                #第一次添加该商品
                my_sku_info = [count, 1]
            else:
                old_count = my_sku_info[0]
                new_count = old_count + count
                if new_count > sku.stock:
                    #检查最新数量是否小于库存
                    return JsonResponse({'code': 10402, 'error': 'The new count is error'})
                my_sku_info[0] = new_count

        print(222222222)
        print(my_sku_info)

        self.set_carts_data(user.id, sku.id, my_sku_info)
        carts_data = self.get_carts_all_data(user.id)
        carts_count = len(carts_data)
        return JsonResponse({'code':200, 'data':{'carts_count':carts_count}, 'base_url': settings.PIC_URL})




    def get(self, request, username):

        #获取购物车数据
        user = request.myuser
        skus_list = self.get_carts_list(user.id)
        return JsonResponse({'code':200, 'data':skus_list, 'base_url':settings.PIC_URL})



    def merge_carts(self, uid, carts_info):

        carts_data = self.get_carts_all_data(uid)

        if not carts_info:
            #用户离线状态下， 未使用购物车
            return len(carts_data)

        for c_dic in carts_info:

            sku_id = int(c_dic['id'])
            try:
                sku_data = SKU.objects.get(id=sku_id, is_launched=True)
            except Exception as e:
                continue
            c_count = int(c_dic['count'])

            #判断后端购物车是否有该商品
            if sku_id in carts_data:
                #后端购物车有该商品
                sku_count = carts_data[sku_id][0]
                last_count = min(sku_data.stock, max(sku_count, c_count))
                carts_data[sku_id][0] = last_count
            else:
                #后端购物车没有该商品
                carts_data[sku_id] = [min(sku_data.stock, c_count), 1]

            self.set_carts_data(uid, sku_id, carts_data[sku_id])

        return len(carts_data)































