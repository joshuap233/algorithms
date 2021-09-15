# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
# 429. N 叉树的层序遍历


from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ret = []
        while q:
            cur = []
            for i in range(len(q)):
                e = q.popleft()
                cur.append(e.val)
                for j in e.children:
                    q.append(j)
            ret.append(cur)
        return ret
