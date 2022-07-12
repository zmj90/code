"""
    可迭代对象工具集
"""


# 如何使用？
# 1. 导入:from common.iterable_tools import IterableHelper
# 2. IterableHelper.方法(容器,lambda item:对列表元素的处理)
class IterableHelper:
    """
        可迭代对象助手:封装对可迭代对象的常用高阶函数
    """

    @staticmethod  # 静态方法:方法内部不需要操作实例成员
    def find_single(iterable, condition):
        """
            在可迭代对象中查找第一个满足条件的元素
        :param iterable: 可迭代对象
        :param condition:函数类型,搜索条件
        :return: 满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中查找所有满足条件的元素
            类似于filter
        :param iterable: 可迭代对象
        :param condition:函数类型,搜索条件
        :return: 生成器对象,推算满足条件的元素
        """

        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def sum(iterable, condition):
        """
            在可迭代对象中根据条件累加
        :param iterable: 可迭代对象
        :param condition:函数类型,累加条件
        :return: 数值类型,累加和
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)
        return sum_value

    @staticmethod
    def select(iterable, condition):
        """
           在可迭代对象中根据条件处理元素，返回处理结果
           类似于map
           :param iterable: 可迭代对象
           :param condition:函数类型,处理条件
           :return: 生成器,推算处理结果
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def delete_all(iterable, condition):
        """

        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):
        """
            类似于max
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def order_by(iterable, condition):
        """
            类似于sort
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
