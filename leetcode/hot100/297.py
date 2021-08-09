# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# 297. 二叉树的序列化与反序列化
# 同一题: leetcode/jian-zhi-offer/37.py
# 这里写层次遍历的方法

import json
from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
        层次遍历
    """

    def serialize(self, root: TreeNode) -> str:
        queue = deque([root])
        res = []

        while queue:
            e = queue.popleft()
            res.append(e.val if e else None)
            if e:
                queue.append(e.left)
                queue.append(e.right)
        return json.dumps(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = json.loads(data)
        if not (nodes and nodes[0] is not None):
            return None

        i = 1
        root = TreeNode(nodes[0])
        queue = deque([root])

        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

