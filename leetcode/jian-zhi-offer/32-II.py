# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
# 剑指 Offer 32 - II. 从上到下打印二叉树 II

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 两个队列,一个存当前层节点,一个存下一层节点
class Solution:
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
        return res


# 方法 2, 重点是 len(queue),这样就不需要定义两个队列
# 两种方法也没多大区别。。。。
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return []

        queue = deque([root])
        while queue:
            r = []
            for _ in range(len(queue)):
                node = queue.popleft()
                r.append(node.val)
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
            res.append(r)
        return res
