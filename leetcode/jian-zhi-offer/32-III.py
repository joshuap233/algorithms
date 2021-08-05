# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
# 剑指 Offer 32 - III. 从上到下打印二叉树 III


from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    在 32-II 的基础上修改了组后的部分：
    即逆序结果
    for i, v in enumerate(res):
        i % 2 == 1 and v.reverse()
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []

        cq, nq = deque([root]), deque()
        cur = []
        while cq or nq:
            if not cq:
                res.append(cur)
                cur = []
                nq, cq = cq, nq

            node = cq.popleft()
            cur.append(node.val)
            node.left and nq.append(node.left)
            node.right and nq.append(node.right)
        res.append(cur)

        for i, v in enumerate(res):
            i % 2 == 1 and v.reverse()
        return res
