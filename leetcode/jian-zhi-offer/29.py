# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
# 剑指 Offer 29. 顺时针打印矩阵


from typing import List


# 将已经打印的元素删除,这样更加方便判断循环退出条件
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        i = 0
        while matrix and matrix[0]:
            if i == 0:
                ret.extend(matrix.pop(0))
            elif i == 1:
                for y in matrix:
                    ret.append(y.pop(-1))
            elif i == 2:
                ret.extend(reversed(matrix.pop(-1)))
            else:
                for y in reversed(matrix):
                    ret.append(y.pop(0))
            i = (i + 1) % 4
        return ret


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        maxX, maxY = len(matrix[0]), len(matrix)
        left, right = 0, maxX - 1
        top, bottom = 0, maxY - 1
        ret = []
        x = y = 0
        while True:
            for x in range(left, right + 1):
                ret.append(matrix[y][x])
            top += 1
            if top > bottom:
                break

            for y in range(top, bottom + 1):
                ret.append(matrix[y][x])
            right -= 1
            if left > right:
                break

            for x in reversed(range(left, right + 1)):
                ret.append(matrix[y][x])
            bottom -= 1
            if top > bottom:
                break

            for y in reversed(range(top, bottom + 1)):
                ret.append(matrix[y][x])
            left += 1
            if left > right:
                break
        return ret


s = Solution()
res = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(res)
