#
#
# @param n long长整型
# @return int整型
#
# https://ac.nowcoder.com/acm/contest/6221/B


# 恩...时间超限
class Solution:
    def work(self, n):
        res = 0
        for i in range(1, n + 1):
            res += n // i
        return res % 998244353


# 整除分块
class Solution2:
    """
        分段
        n/i 恰好等于2的点, i=[n/2],([x]表示向下取整
        [n/2+1,end]段值为1, 段长为n-([n/2]+1)+1=n-[n/2]
        [n/3+1,n/2]段值为2,段长为[n/2]-([n/3+]1) + 1 = [n/2]-[n/3]
        [n/4+1,n/3]段值为3,段长为n/3-(n/4+1)+1 = [n/3] - [n/4]
        ......
        段长和 = n 结束
        计算过程中数字太大,取模 (a + b) % p = (a%p + b%p) %p
    """
    # 还是没通过...实在看不出算法错哪....
    def work(self, n):
        mod = 998244353
        res = 0
        seg = 2
        seg_total_length = 0
        while seg_total_length != n:
            seg_length = n // (seg - 1) - n // seg
            seg_total_length += seg_length
            res = ((seg_length * (seg - 1)) % mod + res) % mod
            seg += 1
        return res % mod


s = Solution2()
print(s.work(10))
