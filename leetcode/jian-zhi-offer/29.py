# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
# 剑指 Offer 29. 顺时针打印矩阵


from typing import List


# 将已经打印的元素删除,这样更加方便判断循环退出条件
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = 0
        while matrix and matrix[0]:
            if i % 4 == 0:
                res.extend(matrix.pop(0))
            elif i % 4 == 1:
                for j in matrix:
                    res.append(j.pop(-1))
            elif i % 4 == 2:
                res.extend(reversed(matrix.pop(-1)))
            else:
                for j in reversed(matrix):
                    res.append(j.pop(0))
            i += 1
        return res


s = Solution()
res = s.spiralOrder([[7], [9], [6]])
print(res)
