import jwt
from django.conf import settings
from django.http import JsonResponse
from user.models import UserProfile


def logging_check(func):
    def wrapper(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")
        print("---------------------------------")
        # print(request.META)
        print("---------------------------------")
        if not token:
            result = {"code": 403, "error": "Please login"}
            return JsonResponse(result)

        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms="HS256")
        except Exception as e:
            print(f"jwt decode error is {e}")
            result = {"code": 403, "error": "Please login"}
            return JsonResponse(result)

        # 神来之笔
        username = res["username"]
        user = UserProfile.objects.get(username=username)
        request.myuser = user

        return func(self, request, *args, **kwargs)

    return wrapper
