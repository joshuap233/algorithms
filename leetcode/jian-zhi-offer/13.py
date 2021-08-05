# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
# 剑指 Offer 13. 机器人的运动范围


# 广搜
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def _sum(v) -> int:
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            return s

        node = [[0] * n for _ in range(m)]
        queue = [(0, 0)]
        cnt = 0
        while queue:
            x, y = queue.pop()
            if x < n and y < m and node[y][x] == 0 and _sum(x) + _sum(y) <= k:
                cnt += 1
                node[y][x] = 1
                queue.append((x + 1, y))
                queue.append((x, y + 1))
        return cnt


s = Solution()
print(s.movingCount(3, 1, 0))
