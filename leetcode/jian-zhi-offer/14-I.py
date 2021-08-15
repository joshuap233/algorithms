# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
# 剑指 Offer 14- I. 剪绳子


# 可以使用 list 与 array 存储,
# 但是 array 访问比 字典慢, 比 list 慢,离谱,但是占用的空间小了
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
        return maps[n]


s = Solution()
print(s.cuttingRope(10))
