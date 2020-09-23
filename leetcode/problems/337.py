# https://leetcode-cn.com/problems/house-robber-iii/

# 337. 打家劫舍 III
# Definition for a binary tree node.
from typing import Dict

from leetcode.helper.tree import TreeNode, generate_tree


class Solution:
    f: Dict[TreeNode, int] = {None: 0}
    g: Dict[TreeNode, int] = {None: 0}

    def rob(self, root: TreeNode) -> int:
        self._rob(root)
        return max(self.f[root], self.g[root])

    def _rob(self, node: TreeNode):
        if node is None:
            return
        self._rob(node.left)
        self._rob(node.right)
        self.f[node] = node.val + self.g[node.left] + self.g[node.right]
        self.g[node] = max(self.f[node.left], self.g[node.left]) + max(self.f[node.right], self.g[node.right])


head = generate_tree([3, 2, 3, None, 3, None, 1])
s = Solution()
print(s.rob(head))
