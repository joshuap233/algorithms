from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recur(node: Node):
            ret.append(node.val)
            for i in node.children:
                recur(i)

        if not root:
            return []
        ret = []
        recur(root)
        return ret


class Solution1:
    """迭代法"""

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        q = deque([root])
        ret = []
        while q:
            e = q.pop()
            ret.append(e.val)
            for i in reversed(e.children):
                q.append(i)
        return ret
