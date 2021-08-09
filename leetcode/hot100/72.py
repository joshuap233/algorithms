# https://leetcode-cn.com/problems/edit-distance/
# 72. 编辑距离


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)

        # right 为需要操作的索引,left 为单词左边界在 word1 中索引
        def recur(left: int, right: int):
            e = word1[right]

            # 删除
            word1[right] = None
            recur(left, right + 1)

            # 替换
            word1[right] = word2[right - left]
            recur(left, right + 1)
            word1[right] = e

            # 在 right 左边插入
            word1.insert(right, word2[right - left])

        recur(0, 0)
