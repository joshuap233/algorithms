# https://leetcode-cn.com/problems/rotate-image/
from typing import List


class Solution:
    """
        这怎么看着像找规律题.....
        a,b,c
        d,e,f
        g,h,i

    -> i f c
       h e b
       g d a

    ->
      g d a
      h e b
      i f c

      先对角对称,然后上下反转,(找对称点麻烦)

      上面的实现麻烦,改成 先上下反转,然后对角线对称((i,j) 对称点为 (j,i))
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 上下反转
        for y in range(n // 2):
            for x in range(n):
                matrix[y][x], matrix[-y - 1][x] = matrix[-y - 1][x], matrix[y][x]

        # 对角反转
        for y in range(n):
            for x in range(y + 1, n):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]


s = Solution()
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
