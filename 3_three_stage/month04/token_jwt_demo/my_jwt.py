import json
import base64
import time
import hmac
import copy


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def encode(self_payload, key, exp=300):
        # init header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        # sepaarators 分隔符号 参数为(), 第一个元素是 键值对之间拿什么分隔，第二个元素是key与value之间拿什么分隔
        # sort_keys 是否要保证json串有序
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        # init payload
        payload = copy.deepcopy(self_payload)
        payload['exp'] = exp + time.time()
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # init sign
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def b64encode(j_s):

        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b_s):

        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def decode(token, key):

        header_bs, payload_bs, sign_bs = token.split(b'.')

        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        if sign_bs != Jwt.b64encode(hm.digest()):
            # 签名部分不一致， token有问题
            raise

        # 检查token是否过期
        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)

        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise

        return payload


if __name__ == '__main__':
    print('---encode is')
    s = Jwt.encode({'username': 'guoxiaonao'}, '123456', exp=3)
    print(s)

    time.sleep(4)

    print('---decode is')
    print(Jwt.decode(s, '123456'))

    import jwt
    jwt.decode()
