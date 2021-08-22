# https://leetcode-cn.com/problems/house-robber-iii/
# 337. 打家劫舍 III

from functools import lru_cache
from typing import List

from leetcode.helper.tree import TreeNode, generate_tree


class Solution:
    """
        直接递归 + lru_cache
        当前节点的最大值:
        为 max((l + r), (p + rr +lr + rl + rr))

         p
     l      r
  ll  lr  rl rr
    """

    @lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        r = root.val
        if root.right:
            r += self.rob(root.right.right) + self.rob(root.right.left)
        if root.left:
            r += self.rob(root.left.left) + self.rob(root.left.right)

        return max(r, self.rob(root.left) + self.rob(root.right))


class Solution1:
    """
        动态规划:
        1. 当前节点偷: 当前节点的钱 + 当前节点左孩子不偷 + 右孩子不偷的钱
        2. 当前节点不偷: 左孩子能偷到的钱 + 右孩子能偷到的钱 (左右孩子可能本身没偷)

        1. 所以可以把偷或者不偷的状态向下传递,但是这么无法统计最大值,
        2. 将偷或不偷的状态向上传递
        [a,b] 表示不偷的钱为 a, 偷的钱为 b
    """

    def rob(self, root: TreeNode) -> int:
        def recur(node: TreeNode) -> List[int]:
            if not node:
                return [0, 0]

            a = recur(node.left)
            b = recur(node.right)

            """
                node.val + a[0] + b[0] 表示偷当前节点,则儿子不能偷
                
                当前节点不偷, 则 可以的组合为:
                a[0] + b[0],a[0]+b[1],a[1]+b[0],a[1]+b[1]
                也就是 max(a[0], a[1]) + max(b[0], b[1])
            """
            return [max(a[0], a[1]) + max(b[0], b[1]), node.val + a[0] + b[0]]

        return max(recur(root))


r = [2, 1, 3, None, 4]
s = Solution1()
s.rob(generate_tree(r))
