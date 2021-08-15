from collections import deque
from typing import List


# 二叉树前序遍历(递归)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recur(root: TreeNode) -> None:
    # do something
    recur(root.left)
    recur(root.right)


# 二叉树中序遍历(递归)

def recur1(root: TreeNode) -> None:
    recur(root.left)
    # do something
    recur(root.right)


# 二叉树后序遍历(递归)

def recur2(root: TreeNode) -> None:
    recur(root.left)
    recur(root.right)
    # do something


# 二叉树前序遍历(迭代)
# 使用栈
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque([root])
        res = []
        while stack:
            e = stack.pop()
            if e:
                res.append(e.val)
                stack.append(e.right)
                stack.append(e.left)
        return res


# 二叉树中序遍历(迭代)
# 使用栈, 一直遍历,直到左子树为 None,过程中将元素添加到栈
# 然后元素 e 出栈, cur = e.right
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque()
        res = []
        while root:
            while root.left:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


# 二叉树后序遍历(迭代)
# 与前序遍历类似,不过最终结果要逆转
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque([root])
        res = []
        while stack:
            e = stack.pop()
            if e:
                res.append(e.val)
                stack.append(e.left)
                stack.append(e.right)
        return res[::-1]
