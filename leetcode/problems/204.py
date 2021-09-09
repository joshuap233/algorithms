# https://leetcode-cn.com/problems/count-primes/
# 204. 计数质数
import math


class Solution:
    """直接暴力解法, 时间超限, 别的语言能过"""

    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            for j in range(2, math.isqrt(i) + 1):
                if i % j == 0:
                    break
            else:
                cnt += 1
        return cnt


class Solution1:
    """
        埃氏筛法(厄拉多塞筛法)
        如果 x 是质数，那么大于 x 的 x 的倍数 2x,3x,…
        一定不是质数

        数 i 从 i * i 开始遍历, 因为 2*i, 3*i, 5*i 必然已经
        被 2,3,5 计算过
    """

    def countPrimes(self, n: int) -> int:
        array = [1] * n
        cnt = 0
        for i in range(2, n):
            if array[i]:
                cnt += 1
                j = i * i
                while j < n:
                    array[j] = 0
                    j += i
        return cnt


s = Solution1()
print(s.countPrimes(10))
