from django.core.cache import caches


# @cache_check(key_prefix='gd', key_param='sku_id', cache='goods_detail', expire=30)


# func = cache_check(**cache_kwargs)(func)
# func(self, request, *args, **kwargs)
def cache_check(**cache_kwagrs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):
            # 获取存储位置
            CACHE = caches['default']
            if "cache" in cache_kwagrs:
                CACHE = caches[cache_kwagrs["cache"]]
            key_prefix = cache_kwagrs["key_prefix"]
            key_param = cache_kwagrs["key_param"]
            expire = cache_kwagrs.get("expire", 30)

            if key_param not in kwargs:
                raise
            cache_key = key_prefix + str(kwargs[key_param])
            print(f"cache key is {cache_key}")
            # 检查缓存
            res = CACHE.get(cache_key)
            if res:
                print(f"return {cache_key} cache")
                return res
            # 没有缓存
            res = func(self, request, *args, **kwargs)
            CACHE.set(cache_key, res, expire)
            return res
        return wrapper
    return _cache_check
