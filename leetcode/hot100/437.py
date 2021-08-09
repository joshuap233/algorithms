# https://leetcode-cn.com/problems/path-sum-iii/
# 437. 路径总和 III
from leetcode.helper.tree import generate_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        前缀和....
        s 记录当前节点到根节点的路径和,
        d 记录之前路径的和出现的次数,
        初始化: Counter([0])
    """

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        from collections import Counter
        cnt = 0

        # s 记录当前节点到根节点的路径和, d 记录之前路径的和
        def recur(node: TreeNode, s: int, sums: Counter):
            nonlocal cnt
            if not node:
                return

            s += node.val
            if sums[s - targetSum] != 0:
                cnt += sums[s - targetSum]

            sums[s] += 1
            recur(node.left, s, sums)
            recur(node.right, s, sums)
            sums[s] -= 1

        recur(root, 0, Counter([0]))
        return cnt


class Solution:
    """
        上面的代码优化下
    """

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        from collections import Counter

        def recur(node: TreeNode, s: int) -> int:
            if not node:
                return 0
            s += node.val
            cnt = sums[s - targetSum]
            sums[s] += 1
            cnt += recur(node.left, s) + recur(node.right, s)
            sums[s] -= 1
            return cnt

        sums = Counter([0])
        return recur(root, 0)


root = generate_tree([0, 1, 1])
s = Solution()
s.pathSum(root, 1)
