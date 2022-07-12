class CommodityModel:
    """
        商品模型:将多个商品信息封装为一个Model类型
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        # 全球唯一标识符(由controller决定)
        self.cid = cid

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

    def __eq__(self, other):
        return self.cid == other
