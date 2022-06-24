from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re

class MyMW(MiddlewareMixin):

    def process_request(self, request):
        #请求到到urls主路由之前，执行当前方法
        #None 正常返回
        #HttpReponse 跳出django 直接返回响应
        print('MyMW process_request do---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        #请求进到视图函数之前 调用
        #返回值 同上
        print('MyMW process_view do---')

    def process_response(self, request, response):
        #任何响应在返回给浏览器之前 均会调用
        #返回值： 必须是response对象
        print('MyMW process_response do ---')
        return response


class MyMW2(MiddlewareMixin):

    def process_request(self, request):
        #请求到到urls主路由之前，执行当前方法
        #None 正常返回
        #HttpReponse 跳出django 直接返回响应
        print('MyMW2 process_request do---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        #请求进到视图函数之前 调用
        #返回值 同上
        print('MyMW2 process_view do---')

    def process_response(self, request, response):
        #任何响应在返回给浏览器之前 均会调用
        #返回值： 必须是response对象
        print('MyMW2 process_response do ---')
        return response

class VisitLimit(MiddlewareMixin):

    visit_times = {}

    def process_request(self, request):

        ip_address = request.META['REMOTE_ADDR']
        #/test_mw  /test开头的地址都要限制
        if not re.match(r'^/test', request.path_info):
            return

        times = self.visit_times.get(ip_address, 0)
        print('IP %s 已经访问了 %s 次'%(ip_address, times))
        if times >= 5:
            return HttpResponse('!!!!!对不起')

        self.visit_times[ip_address] = times + 1













