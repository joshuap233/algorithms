# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
# 剑指 Offer 14- II. 剪绳子 II

class Solution:
    maps = {2: 2, 3: 3, 4: 4}

    def cuttingRope(self, n: int) -> int:
        maps = self.maps

        if n < 4:
            return n - 1

        for i in range(5, n + 1):
            if i not in maps:
                maps[i] = max(
                    maps[i - 2] * 2,
                    maps[i - 3] * 3,
                )
        return maps[n] % 1000000007


s = Solution()
res = s.cuttingRope(120)
print(res)
