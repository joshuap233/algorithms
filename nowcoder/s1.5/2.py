# https://ac.nowcoder.com/acm/contest/6488/B
# 恩....看到乘方写成了i**i 一直没通过,差点怀疑人生...


class Solution:

    def __init__(self):
        self.memo = self.get_all()

    def solve(self, x):
        return x in self.memo

    @staticmethod
    def get_all():
        return set((i * i) % 1000 for i in range(1000))


s = Solution()
print(s.solve(24))
