from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMW(MiddlewareMixin):
    ip_dict = {}
    def process_request(self, request):
        url = request.path_info
        if "/test_mw" in url:
            if (ip := request.META['REMOTE_ADDR']) not in MyMW.ip_dict:
                MyMW.ip_dict[ip] = 1
            else:
                MyMW.ip_dict[ip] += 1
                if MyMW.ip_dict[ip] > 5:
                    print(MyMW.ip_dict[ip])
                    return HttpResponse("不允许访问")
        # print("process_request")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process_view")

    def process_response(self,request, response):
        print("process_response")
        return response


# class MyMW2(MiddlewareMixin):
#     def process_request(self, request):
#         print("process_request2")
#
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         print("process_view2")
#
#     def process_response(self,request, response):
#         print("process_response2")
#         return response
#
#
# class MyMW3(MiddlewareMixin):
#     def process_request(self, request):
#         print("process_request3")
#
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         print("process_view3")
#
#     def process_response(self,request, response):
#         print("process_response3")
#         return response