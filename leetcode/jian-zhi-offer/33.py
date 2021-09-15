# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
# 剑指 Offer 33. 二叉搜索树的后序遍历序列

from typing import List


# 后续遍历特点: 后续遍历值的集合为 values, values[-1] 为根
# 有索引 i, values[i] 左边的数为根的左字树,右边的数为根的右子树(包括values[i]),
# 所以找到 i,判断 i 右边的树是否小于根值,然后递归判断每个子树
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(nodes: list) -> bool:
            if len(nodes) <= 1:
                return True

            root = nodes[-1]
            i = 0
            while i < len(nodes) - 1 and nodes[i] < root:
                i += 1

            for j in range(i, len(nodes) - 1):
                if nodes[j] <= root:
                    return False

            return recur(nodes[:i]) and recur(nodes[i:len(nodes) - 1])

        return recur(postorder)


# 上面方法的优化
class Solution1:
    def verifyPostorder(self, nodes: List[int]) -> bool:
        def recur(left: int, right: int) -> bool:
            if right <= left:
                return True

            root = nodes[right]
            i = left
            while i < right and nodes[i] < root:
                i += 1

            for j in range(i, right):
                if nodes[j] <= root:
                    return False

            return recur(left, i - 1) and recur(i, right - 1)

        return recur(0, len(nodes) - 1)
