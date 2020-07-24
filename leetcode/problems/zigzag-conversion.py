# 字形变换
# https://leetcode-cn.com/problems/zigzag-conversion/


# 68 ms
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 子数组为row(x)
        down = True
        row = -1  # 一个子数组为一行
        rows = list(map(lambda _: [], range(numRows)))
        for index, string in enumerate(s):
            if down:
                row += 1
            else:
                row -= 1
            rows[row].append(string)
            if row + 1 == numRows:
                down = False
            if row == 0:
                down = True
        res = ''
        for r in rows:
            for string in r:
                if string != '':
                    res = res + string
        return res


s = Solution()
print(s.convert("ABCDEFG", 2))
