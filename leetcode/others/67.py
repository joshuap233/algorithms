# 帕斯卡三角形

from typing import List


# 40 ms
class Solution:
    memo: List[List[int]] = [[1], [1, 1]]

    def generate(self, n: int) -> List[List[int]]:
        level = len(self.memo)
        if n <= level:
            return self.memo[:n]
        for i in range(level, n):
            pre_rows = self.memo[i - 1]
            new_row: List[int] = [1]
            for item in range(1, i):
                new_row.append(pre_rows[item - 1] + pre_rows[item])
            new_row.append(1)
            self.memo.append(new_row)
        return self.memo


s = Solution()
print(s.generate(0))
print(s.generate(1))
print(s.generate(2))
print(s.generate(4))
print(s.generate(3))
