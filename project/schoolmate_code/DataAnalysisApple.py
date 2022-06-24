# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re


class AppleAppleApple:
    """苹果数据分析"""

    def __init__(self):
        pass

    @staticmethod
    def sift_apples(df):
        """
        筛选苹果农产品
        需求: 剔除非苹果农产品的商品，如：苹果手机
        """

        df = df.loc[                                                            # 使用 pandas loc方法查询
            (df['third_cat'] == '水果') &                                       # 查询 'third_cat'字段为 '水果'
            (df['forth_cat'] == '苹果') &                                       # 查询 'forth_cat'字段为 '苹果'
            (df['agri_thirdcat'] == '苹果') &                                   # 查询 'agri_thirdcat'字段为 '苹果'
            (df['agri_seccat'] == '鲜果类') &                                   # 查询 'agri_seccat'字段为 '鲜果类'
            (df['agri_firstcat'] == '水果')                                     # 查询 'agri_firstcat' 字段为 '水果'
                ]

        return df

    @staticmethod
    def net_weight(df):
        """
        解析规格(净含量)数据
        需求: 从detail字段解析每个产品的规格，如果没有规格则标记0
        """

        def net_weight_analysis(net_weight_list_data):
            """
            解析净含量具体的数据
            net_weight_list: 正则匹配出的'规格'和'净含量'列表
            """

            # 如果同时存在 '规格' 和 '净含量' 取 '净含量'
            data = False                                                        # 定义data初始变量
            for i in net_weight_list_data:                                      # 循环正则匹配出来的列表
                if '净含量' in i:                                               # 如果存在净含量
                    data = i                                                    # 给data重新赋值
            if not data:                                                        # 如果data仍然=False
                data = net_weight_list_data[0]                                  # 让data=列表第0个元素

            # 解析出具体的值
            net_weight_data = re.findall(':"(.+?)"$', data)[0].strip()          # 正则取出值并去空格

            # 换算 kg 和 公斤
            if 'kg' in net_weight_data or '公斤' in net_weight_data:            # 如果 kg 或 公斤 在字符串里
                number = re.findall(r'\d+', net_weight_data)[0]                 # 正则取出数字
                net_weight_data = str(int(number) * 1000) + 'g'                 # 换算成 g

            # 换算斤
            if re.findall(r'\d斤', net_weight_data):                            # 如果正则匹配到 '数字+斤'(排除匹配到公斤的情况)
                number = re.findall(r'\d+', net_weight_data)[0]                 # 取出数字
                net_weight_data = str(int(number) * 500) + 'g'                  # 换算成 g

            return net_weight_data

        df['prod_detail'].replace(np.nan, False, inplace=True)                  # 填充prod_detail列的空值为False
        df['net_weight'] = 0                                                    # 添加净含量列全部为0
        df.reset_index(drop=True, inplace=True)                                 # 重置index
        net_weight_index = list(df.columns).index('net_weight')                 # 获取net_weight的横向index编号

        for index, row in df.iterrows():                                        # 遍历DataFrame
            row_data = row['prod_detail']                                       # prod_detail字段的值
            if row_data:                                                        # 如果prod_detail不为空
                net_weight_list = re.findall(                                   # 正则查找'净含量'和'规格'
                    '"净含量":".+?"|"规格":".+?"', row_data)
                if net_weight_list:                                             # 如果正则匹配到的列表不为空
                    net_weight = net_weight_analysis(net_weight_list)           # 交给分析函数处理
                    df.iloc[index, net_weight_index] = net_weight               # 修改'net_weight'字段的数据为net_weight
        return df

    @staticmethod
    def sales_fill(df):
        """
        填充销售字段
        需求: 月销量和月销售额的空值用前一个月的销售额填充
        
        注 :
            只用前一个月填充后一个月在逻辑上覆盖不了
            如果第一个月就没有那后面的数据还是有缺失值
            需要正向填充一次, 再反向填充一次
            用填充的方式去计算价格和排名, 会对真实的计算结果造成影响, 好的解决方案是不填充, 有缺失值的数据不纳入计算
        """

        # 正向填充 1-12月顺序
        for i in range(1, 12):                                                  # 循环1-11月
            previous_month = str(i)                                             # 前一个月str
            next_month = str(i + 1)                                             # 后一个月str
            if len(previous_month) == 1:                                        # 如果字符的长度=1 前面加个0
                previous_month = '0' + previous_month
            if len(next_month) == 1:                                            # 如果字符的长度=1 前面加个0
                next_month = '0' + next_month

            # 填充销售量
            df["month_amount_" + next_month].fillna(                            # pandas fillna 方法填充, 用前一个月填充后一个月
                df["month_amount_" + previous_month],
                inplace=True)

            # 填充销售额
            df["month_money_" + next_month].fillna(                             # pandas fillna 方法填充, 用前一个月填充后一个月
                df["month_money_" + previous_month],
                inplace=True)

        # 反向填充 12-1月顺序
        for i in range(12, 1, -1):                                              # 循环12-1月
            previous_month_reverse = str(i)                                     # 前一个月str
            next_month_reverse = str(i - 1)                                     # 后一个月str
            if len(previous_month_reverse) == 1:                                # 如果字符的长度=1 前面加个0
                previous_month_reverse = '0' + previous_month_reverse
            if len(next_month_reverse) == 1:                                    # 如果字符的长度=1 前面加个0
                next_month_reverse = '0' + next_month_reverse

            # 填充销售量
            df["month_amount_" + next_month_reverse].fillna(                    # pandas fillna 方法填充, 用前一个月填充后一个月
                df["month_amount_" + previous_month_reverse],
                inplace=True)

            # 填充销售额
            df["month_money_" + next_month_reverse].fillna(                     # pandas fillna 方法填充, 用前一个月填充后一个月
                df["month_money_" + previous_month_reverse],
                inplace=True)

        return df


def main():
    a = AppleAppleApple()
    df = pd.read_csv('datasets.csv')

    df = a.sift_apples(df)      # 剔除非苹果农产品的商品，如：苹果手机
    df = a.net_weight(df)       # 从detail字段解析每个产品的规格，如果没有规格则标记0
    df = a.sales_fill(df)       # 月销量和月销售额的空值用前一个月的销售额填充
    df.to_excel('data.xlsx', index=False)
    df.to_csv('data.csv', index=False)


if __name__ == "__main__":
    main()
