"""
   改为标准装饰器
"""

def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        result = func(*args,**kwargs) # 调用旧功能
        return result
    return wrapper

@verify_permissions  # insert = verify_permissions(insert)
def insert(data):
    print("插入")

@verify_permissions # delete = verify_permissions(delete)
def delete():
    print("删除")
    return True

print(delete()) # 调用内函数
insert("新数据")
