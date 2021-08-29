# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# 230. 二叉搜索树中第K小的元素

from leetcode.helper.tree import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ret = None

        def recur(node: TreeNode):
            nonlocal k, ret
            if not node or (ret is not None):
                return None

            recur(node.left)

            k -= 1
            if k == 0:
                ret = node.val

            return recur(node.right)

        recur(root)
        return ret


class Solution1:
    """迭代"""

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(-1)
            k -= 1
            if k == 0:
                return root.val

            root = root.right
