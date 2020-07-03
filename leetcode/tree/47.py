#   二叉树的最大深度
from tree import generate_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_deep = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.find_max_deep(root, deep=0)
        return self.max_deep

    def find_max_deep(self, node, deep):
        deep += 1

        if node.left is None:
            if deep > self.max_deep:
                self.max_deep = deep
        else:
            self.find_max_deep(node.left, deep)

        if node.right is None:
            if deep > self.max_deep:
                self.max_deep = deep
        else:
            self.find_max_deep(node.right, deep)


root = generate_tree([3, 9, 20, None, None, 15, 7])
s = Solution()
print(s.maxDepth(root))
