# https://leetcode-cn.com/problems/same-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.same = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self._traverse(p, q)
        return self.same

    def _traverse(self, node1: [None, TreeNode], node2: [None, TreeNode]):
        if not self.same or (node1 is None and node2 is None):
            return

        if (node1 is None and node2 is not None) or (node2 is None and node1 is not None) or node2.val != node1.val:
            self.same = False
            return
        self._traverse(node1.left, node2.left)
        self._traverse(node1.right, node2.right)
