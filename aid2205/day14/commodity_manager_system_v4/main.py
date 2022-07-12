from usl import CommodityView

# 如果当前是主模块,才启动项目
# （当前模块被导入时不执行）
if __name__ == '__main__':
    view = CommodityView()
    view.main()
