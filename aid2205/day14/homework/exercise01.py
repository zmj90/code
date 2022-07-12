"""
    小明使用手机打电话
        还有可能使用座机...

    封装【分】：创建Person、MobilePhone、Landine
    继承【隔】：创建CommunicationDevice隔离创建Person与MobilePhone、Landine的变化
    多态【做】:Person调用CommunicationDevice
             执行MobilePhone、Landine
    目标：增加新设备,Person不受影响
"""


# -------------------------------
# 小鸭子原则
# 鸭子嘎嘎叫
# 如果狗也会嘎嘎叫,那么狗是一种鸭子
# 如果猫也会嘎嘎叫,那么猫是一种鸭子
# 意义：忽略类型,重视行为。
# 通俗：不继承父类,但具有父类行为,
#      也可以传入到客户端代码
# 优点：代码灵活
# 缺点：代码可读性差

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, device):
        print("打电话")
        # 编码时调用父方法(想想)
        # 运行时执行子方法(实际)
        # 工具.呼叫()
        device.invoke()

class CommunicationDevice:
    def invoke(self):
        pass

class MobilePhone(CommunicationDevice):
    def invoke(self):
        print("手机-呼叫")

class Landine:
    def invoke(self):
        print("座机-呼叫")

xm = Person("小明")
xw = Person("小王")
xm.call(MobilePhone())
xm.call(Landine())
