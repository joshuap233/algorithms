# 剑指 Offer 34. 二叉树中和为某一值的路径
# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    `   树的根节点开始往下一直到叶节点所经过的节点形成一条路径
        必须是到叶子节点的路径
    """

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def backtrace(node: TreeNode, s: int):
            if not node:
                return

            cur.append(node.val)
            s += node.val
            if not (node.left or node.right):
                if s == target:
                    ret.append(cur[:])
            else:
                backtrace(node.left, s)
                backtrace(node.right, s)
            cur.pop()

        ret = []
        cur = []
        backtrace(root, 0)
        return ret
