"""
    闭包-应用
        有外有内：外函数得钱,内函数花钱
        内使用外：内函数花钱时需要扣除得到的钱
        外返回内：需要返回花钱的行为才能灵活的购买需要的商品

        逻辑连续：从得钱,到花钱,逻辑连续不中断
"""


def give_new_year_money(money):  # 得钱
    print(f"获得{money}压岁钱")

    def child_buy(commodity, price):  # 花钱
        nonlocal money
        money -= price
        print(f"购买了{commodity}商品,花了{price},还剩下{money}")

    # child_buy("变形金刚", 300) # 不调用内部函数
    return child_buy  # 返回内部函数


action = give_new_year_money(1000)
action("变形金刚", 300)
action("工程车", 100)
action("挖掘机", 200)
