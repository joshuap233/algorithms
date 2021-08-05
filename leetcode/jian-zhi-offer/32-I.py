# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
# 剑指 Offer 31. 栈的压入、弹出序列


from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        queue = deque([root])
        while queue:
            node = queue.popleft()
            res.append(node.val)
            node.left and queue.append(node.left)
            node.right and queue.append(node.right)
        return res
