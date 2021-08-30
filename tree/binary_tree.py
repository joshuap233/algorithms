from collections import deque
from typing import List


# 二叉树前序遍历(递归)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        stack = deque([root])
        res = []
        while stack:
            e = stack.pop()
            if e:
                res.append(e.val)
                stack.append(e.right)
                stack.append(e.left)
        return res

    def preorderTraversal2(self, root: TreeNode) -> None:
        # 递归
        print(root.val)
        self.preorderTraversal2(root.left)
        self.preorderTraversal2(root.right)


# 中序遍历
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
            二叉树中序遍历(迭代)
            使用栈, 一直遍历,直到左子树为 None,过程中将元素添加到栈
            然后元素 e 出栈, cur = e.right
        """
        stack = deque()
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> None:
        # 递归
        self.inorderTraversal2(root.left)
        print(root.val)
        self.inorderTraversal2(root.right)


# 二叉树后序遍历(迭代)
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代,与前序遍历类似,不过最终结果要逆转
        stack = deque([root])
        res = []
        while stack:
            e = stack.pop()
            if e:
                res.append(e.val)
                stack.append(e.left)
                stack.append(e.right)
        return res[::-1]

    def postorderTraversal2(self, root: TreeNode) -> None:
        # 递归
        self.postorderTraversal2(root.left)
        self.postorderTraversal2(root.right)
        print(root.val)
