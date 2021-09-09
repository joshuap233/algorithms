# https://leetcode-cn.com/problems/diagonal-traverse/
# 498. 对角线遍历

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = []
        maxX, maxY = len(mat[0]), len(mat)
        i = 0
        x, y = 0, 0

        for x in range(maxX):
            cur = []
            ty = y
            while x >= 0 and ty < maxY:
                cur.append(mat[ty][x])
                x -= 1
                ty += 1
            ret.extend(reversed(cur) if i % 2 == 0 else cur)
            i += 1

        for y in range(1, maxY):
            cur = []
            x = maxX - 1
            while x >= 0 and y < maxY:
                cur.append(mat[y][x])
                x -= 1
                y += 1
            ret.extend(reversed(cur) if i % 2 == 0 else cur)
            i += 1

        return ret


class Solution1:
    """模拟法"""

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = []
        maxX, maxY = len(mat[0]), len(mat)
        n = maxY * maxX
        x, y = 0, 0
        for _ in range(n):
            ret.append(mat[y][x])
            if (y + x) % 2 == 0:
                # 向上
                # 到达右边界(包括到达右上角)
                if x == maxX - 1:
                    y += 1
                # 到达上边界
                elif y == 0:
                    x += 1
                else:
                    y -= 1
                    x += 1
            else:
                if y == maxY - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    y += 1
                    x -= 1
        return ret


s = Solution1()
print(s.findDiagonalOrder(
    [[2, 3]]
))
