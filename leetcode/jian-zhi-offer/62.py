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
        设剩下的数字为 A,
        剩余数字个数为 1 时, A 的位置为 0
        剩余数字个数为 2 时, A 的位置为 (0+m)%2
        剩余数字个数为 3 时, A 的位置为 ((0+m)%2+m)%3
        剩余数字个数为 4 时, A 的位置为 (((0+m)%2+m)%3)%4
        .....
        n 此后, A 的位置为 A 在初始数组中的索引
    """

    def lastRemaining(self, n: int, m: int) -> int:
        pos = 0
        for i in range(2, n + 1):
            pos = (pos + m) % i
        return pos


s = Solution1()
s.lastRemaining(5, 3)
