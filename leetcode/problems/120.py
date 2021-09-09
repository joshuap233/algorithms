# https://leetcode-cn.com/problems/triangle/
# 120. 三角形最小路径和
from typing import List


class Solution:
    """
        二叉树最短路径
        你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
        时间超限......
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        maxY = len(triangle)

        def recur(x: int, y: int) -> int:
            if not (y < maxY and x < len(triangle[y])):
                return float('inf')

            if y == maxY - 1:
                return triangle[y][x]

            return triangle[y][x] + min(
                recur(x, y + 1),
                recur(x + 1, y + 1)
            )

        return recur(0, 0)


class Solution1:
    """
        上面算法的修改, 自顶向下, 直接将路径值存储到父节点处,
        很慢....时间复杂度 O(n*n)
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for y in range(1, len(triangle)):
            # 哨兵节点
            triangle[y - 1].append(float('inf'))
            for x, v in enumerate(triangle[y]):
                triangle[y][x] = triangle[y][x] + min(
                    triangle[y - 1][x],
                    triangle[y - 1][x - 1]
                )
        return min(triangle[-1])


class Solution2:
    """
        上面算法的优化,自底向上, 不需要 min(triangle[-1]), 也不需要判断边界
    """

    def minimumTotal(self, tri: List[List[int]]) -> int:
        for j in range(len(tri) - 2, -1, -1):
            for i in range(len(tri[j])):
                tri[j][i] = min(tri[j + 1][i], tri[j + 1][i + 1]) + tri[j][i]
        return tri[0][0]
