from typing import List

from leetcode.tree.tree import TreeNode, generate_tree


# 递归
class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.recursive(root)
        return self.res

    def recursive(self, node: TreeNode):
        if node is None:
            return
        self.recursive(node.left)
        self.recursive(node.right)
        self.res.append(node.val)


# 迭代
class Solution2:
    def __init__(self):
        self.stack = []
        self.res = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.stack = [root]
        while self.stack is not None:
            pass


s = Solution()
head = generate_tree([1, None, 2, 3])
print(s.postorderTraversal(head))
