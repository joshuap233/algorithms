"""
    希尔排序是冲破二次时间屏障的第一批算法
    希尔排序通过比较相距一定间隔的元素来工作,
    各趟比较所用距离随着算法进行而减小,
    因此希尔排序又叫缩小增量排序

    希尔排序使用一个序列 h1, h2, ... hk 叫做增量序列,
    只要 h1 = 1, 任何增量序列都是可行的,不过有些增量比另外一些要好

    希尔排序是插入排序的优化, 在使用增量 hk 进行一趟排序之后,
    保证所有间隔 hk 的元素都被排序. 一趟 hk 排序的作用就是
    对 hk 个独立子数组执行一次插入排序

"""

from typing import List


def shellSort(nums: List[int]) -> List[int]:
    pass
