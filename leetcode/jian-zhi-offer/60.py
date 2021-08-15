# https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
# 剑指 Offer 60. n个骰子的点数

from typing import List
from collections import Counter


# 暴力解法,时间超限
class Solution:
    counter = [Counter() for i in range(11)]

    def dicesProbability(self, n: int) -> List[float]:
        counter = Counter()

        def recur(value, num):
            if num == 0:
                counter[value] += 1
                return

            for j in range(1, 7):
                recur(value + j, num - 1)

        recur(0, n)

        res = []
        length = 6 ** n

        for i in range(1 * n, 6 * n + 1):
            res.append(counter[i] / length)
        return res


class Solution1:
    """
        解法: 先计算一个骰子所有结果统计,
        然后利用上一个骰子结果统计,计算下一个骰子结果与计数

        计算方法:
            new[v + j] += self.counter[i - 1][v]
    """
    counter = [Counter([i for i in range(1, 7)])]

    def dicesProbability(self, n: int) -> List[float]:
        for i in range(len(self.counter), n):
            new = Counter()
            for v in self.counter[i - 1]:
                for j in range(1, 7):
                    new[v + j] += self.counter[i - 1][v]
            self.counter.append(new)

        counter = self.counter[n - 1]
        length = 6 ** n
        res = []
        for i in range(1 * n, 6 * n + 1):
            res.append(counter[i] / length)
        return res


class Solution2:
    """
        优化上面的解法,减少空间复杂度
        使用数组替代 Counter
    """

    def dicesProbability(self, n: int) -> List[float]:
        last = [1] * 6

        for i in range(2, n + 1):
            new = [0] * (5 * i + 1)  # 6*n-1*n+1
            for v in range(len(last)):
                for j in range(6):
                    new[v + j] += last[v]
            last = new

        length = 6 ** n
        for i, v in enumerate(last):
            last[i] = last[i] / length
        return last


class Solution3:
    """
        优化上面的解法
        存概率,而不是存计数
    """

    def dicesProbability(self, n: int) -> List[float]:
        last = [1 / 6] * 6

        for i in range(2, n + 1):
            new = [0] * (5 * i + 1)  # 6*n-1*n+1
            for v in range(len(last)):
                for j in range(6):
                    new[v + j] += last[v] / 6
            last = new
        return last



s = Solution2()
s.dicesProbability(2)
