# https://leetcode-cn.com/problems/deepest-leaves-sum/
# 1302. 层数最深叶子节点的和
from leetcode.helper.tree import TreeNode
from collections import deque


class Solution:
    """
        层序遍历无法判断是否达到最后一层,
        因此计算每层节点的和
    """
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ret = 0
        q = deque([root])
        while q:
            cur = 0
            for _ in range(len(q)):
                e = q.popleft()
                cur += e.val
                e.left and q.append(e.left)
                e.right and q.append(e.right)
            ret = cur
        return ret
