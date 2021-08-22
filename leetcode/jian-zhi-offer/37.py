# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/
# 剑指 Offer 37. 序列化二叉树


import json
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
        存前序遍历与中序遍历的值,然后重建二叉树
        存 id 来查找根节点
    """

    def serialize(self, root: TreeNode) -> str:
        p, m = [], []  # 前序遍历与中序遍历

        def recur(node: TreeNode):
            if not node:
                return
            p.append((node.val, id(node)))
            recur(node.left)
            m.append((node.val, id(node)))
            recur(node.right)

        recur(root)
        return json.dumps([p, m])

    def deserialize(self, data: str) -> TreeNode:
        n = json.loads(data)
        p, m = n[0], n[1]

        def rebuild(pre: list, mid: list) -> Optional[TreeNode]:
            if not mid:
                return None

            # 二叉树元素可能重复,使用 id 查找
            root = TreeNode(int(pre[0][0]))
            index = mid.index(pre[0])
            root.left = rebuild(pre[1:1 + index], mid[:index])
            root.right = rebuild(pre[1 + index:], mid[index + 1:])
            return root

        return rebuild(p, m)


s = Codec()
s.deserialize('[[1, 2, 3, 4, 5], [2, 1, 4, 3, 5]]')
