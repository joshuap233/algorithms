# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
# 求根节点到叶节点数字之和
from leetcode.helper.tree import TreeNode, generate_tree


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def recur(node: TreeNode, prefix: int) -> int:
            if not node:
                return 0

            if not (node.left or node.right):
                return prefix * 10 + node.val

            prefix = prefix * 10 + node.val
            return recur(node.left, prefix) + recur(node.right, prefix)

        return recur(root, 0)


r = generate_tree([1, 0])
s = Solution()
s.sumNumbers(r)
