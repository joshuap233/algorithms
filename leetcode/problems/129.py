# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
from leetcode.helper.tree import TreeNode, generate_tree


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ret = 0

        def recur(s: int, node: TreeNode):
            nonlocal ret
            if not node:
                return

            s = s * 10 + node.val
            if not (node.left or node.right):
                ret += s
                return

            recur(s, node.left)
            recur(s, node.right)

        recur(0, root)
        return ret


r = generate_tree([1, 0])
s = Solution()
s.sumNumbers(r)
