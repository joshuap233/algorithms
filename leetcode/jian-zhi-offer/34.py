# 剑指 Offer 34. 二叉树中和为某一值的路径
# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 树的根节点开始往下一直到叶节点所经过的节点形成一条路径
# 必须是到叶子节点的路径
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []

        if not root:
            return res

        def recur(node: TreeNode, path: list, tg: int):
            tg -= node.val
            path = path[:]
            path.append(node.val)

            if not node.left and not node.right and tg == 0:
                res.append(path)
            node.left and recur(node.left, path, tg)
            node.right and recur(node.right, path, tg)

        recur(root, [], target)
        return res


# 优化 path 的复制次数(使用回溯)
class Solution1:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        path = []

        if not root:
            return res

        def recur(node: TreeNode, tg: int):
            tg -= node.val
            path.append(node.val)

            if not node.left and not node.right and tg == 0:
                res.append(path[:])
            node.left and recur(node.left, tg)
            node.right and recur(node.right, tg)
            path.pop(-1)

        recur(root, target)
        return res
