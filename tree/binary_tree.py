from collections import deque
from typing import List


# 二叉树前序遍历(递归)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution0:
    """
    看到一个容易理解与记忆的迭代版本：
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    先序中序后续只需要修改 i.val 的位置即可
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """中序"""
        stack = [root]
        ret = []
        while stack:
            i = stack.pop(-1)
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                ret.append(i)
        return ret

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """先序"""
        stack = [root]
        ret = []
        while stack:
            i = stack.pop(-1)
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.left, i.val])
            elif isinstance(i, int):
                ret.append(i)
        return ret

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """后序遍历"""
        stack = [root]
        ret = []
        while stack:
            i = stack.pop(-1)
            if isinstance(i, TreeNode):
                stack.extend([i.val, i.right, i.left])
            elif isinstance(i, int):
                ret.append(i)
        return ret

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ret = []
        while q:
            for i in range(len(q)):
                e = q.popleft()
                ret.append(e.val)
                e.left and q.append(e.left)
                e.right and q.append(e.right)
        return ret


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
