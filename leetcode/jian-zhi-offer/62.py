# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
# 剑指 Offer 62. 圆圈中最后剩下的数字


# 时间超限
class Solution:
    """"
        第一个删除的数字索引为
            index = (m - 1)%len(ll)
        第二个删除的数字索引为:
            index = (index+ m-1)%len(ll)
    """

    def lastRemaining(self, n: int, m: int) -> int:
        ll = list(range(n))
        index = 0
        while len(ll) > 1:
            index = (index + m - 1) % len(ll)
            ll.pop(index)
            index % len(ll)
        return ll[0]


class Solution1:
    """
        直接把公式抄过来的了....
        dp[i]=(dp[i−1]+m)%i
    """

    def lastRemaining(self, n: int, m: int) -> int:
        c = 0
        for i in range(2, n + 1):
            c = (m + c) % i
        return c


s = Solution1()
s.lastRemaining(5, 3)
