# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
# 剑指 Offer 36. 二叉搜索树与双向链表


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 先将节点保存到列表(中序遍历),然后遍历存节点的列表,连接节点
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        nodes = []

        def recur(node: Node):
            if not node:
                return
            recur(node.left)
            nodes.append(node)
            recur(node.right)

        recur(root)

        for i, node in enumerate(nodes):
            node.left = nodes[i - 1]
            node.right = nodes[(i + 1) % len(nodes)]
        return nodes[0]


# 在 recur(node.left) 与 recur(node.right), node 为中序遍历的当前节点,
# 而 prev 为上个中序遍历的节点
class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        prev, head = None, None

        def recur(node: Node):
            nonlocal prev, head
            if not node:
                return

            recur(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node
            prev = node

            recur(node.right)

        recur(root)
        head.left = prev
        prev.right = head

        return head
