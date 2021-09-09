# https://leetcode-cn.com/problems/clone-graph/
# 133. 克隆图

import copy
from typing import List
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: List['Node'] = neighbors or []


class Solution:
    """
        广搜
        使用 dict 记录 old: new 节点映射
        广搜队列存储 (new,old)
    """

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        ret = Node(node.val)
        q = deque([(ret, node)])
        s = {node: ret}
        while q:
            cpy, old = q.popleft()
            for i in old.neighbors:
                if i not in s:
                    new = Node(i.val)
                    q.append((new, i))
                    s[i] = new
                cpy.neighbors.append(s[i])
        return ret


class Solution1:
    """
        深搜
    """

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        s = {}

        def dfs(old: 'Node') -> 'Node':
            if old not in s:
                new = Node(old.val)
                s[old] = new
                new.neighbors = [dfs(i) for i in old.neighbors]
            return s[old]

        return dfs(node)


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return copy.deepcopy(node)
