# https://leetcode-cn.com/problems/chou-shu-lcof/
# 剑指 Offer 49. 丑数


# 使用堆存储, 然后一次 pop, 使用 set 防止重复元素被添加
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heapify, heappop, heappush
        heap = [1, 2, 3, 5]
        s = set(heap)
        heapify(heap)
        for i in range(n - 1):
            v = heappop(heap)
            for j in [2, 3, 5]:
                _next = j * v
                if _next not in s:
                    heappush(heap, _next)
                    s.add(_next)
        return heappop(heap)


# 上面方法的优化,避免出现重复的方法:
# 质数的线性筛算法的精髓在于保存下每一个合数的最小质因子,
# 只能乘以不超过最小质因子的质数, 去生成新的合数, 从而可以避免重复生成相同的合数.
class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heapify, heappop, heappush
        if n == 1:
            return n

        heap = [(2, 2), (3, 3), (5, 5)]
        heapify(heap)
        v = 0
        for i in range(n - 1):
            v, e = heappop(heap)
            if e >= 2:
                heappush(heap, (v * 2, 2))
                if e >= 3:
                    heappush(heap, (v * 3, 3))
                    if e >= 5:
                        heappush(heap, (v * 5, 5))
        return v


s = Solution1()
s.nthUglyNumber(10)
