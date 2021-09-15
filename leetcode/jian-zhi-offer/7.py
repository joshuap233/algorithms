# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
# 剑指 Offer 07. 重建二叉树
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre: List[int], ino: List[int]):
            if not pre:
                return None
            node = TreeNode(pre[0])
            idx = ino.index(pre[0])
            node.left = build(pre[1:idx + 1], ino[:idx])
            node.right = build(pre[idx + 1:], ino[idx + 1:])
            return node

        return build(preorder, inorder)


s = Solution()
print(s.buildTree([1, 2], [2, 1]))
