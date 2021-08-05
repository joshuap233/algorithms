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
        def build(pre, ino) -> Optional[TreeNode]:
            if not pre:
                return None

            rv = pre[0]
            root = TreeNode(rv)
            if len(pre) == 1:
                return root

            i = ino.index(rv)
            root.left = build(pre[1:1 + i], ino[:i])
            root.right = build(pre[1 + i:], ino[i + 1:])
            return root

        return build(preorder, inorder)


s = Solution()
print(s.buildTree([1, 2], [2, 1]))
