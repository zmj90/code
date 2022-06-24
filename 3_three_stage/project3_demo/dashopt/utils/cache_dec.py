from django.core.cache import caches


#/v1/goods/detail/3

#gd_3


#@cache_check(key_prefix='gd', key_param='sku_id', cache='goods_detail',expire=30)

def cache_check(**cache_kwagrs):
    def _cache_check(func):
        def wrapper(self, request, *args, **kwargs):
            #获取存储位置
            CACHE = caches['default']
            if 'cache' in cache_kwagrs:
                CACHE = caches[cache_kwagrs['cache']]
            key_prefix = cache_kwagrs['key_prefix']
            key_param = cache_kwagrs['key_param']
            expire = cache_kwagrs.get('expire', 30)

            if key_param not in kwargs:
                raise
            cache_key = key_prefix + str(kwargs[key_param])
            print('cache key is %s'%(cache_key))
            #检查缓存
            res = CACHE.get(cache_key)
            if res:
                print('return %s cache'%(cache_key))
                return res
            #没有缓存
            res = func(self, request, *args, **kwargs)
            CACHE.set(cache_key, res, expire)
            return res
        return wrapper
    return _cache_check

