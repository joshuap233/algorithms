# https://leetcode-cn.com/problems/maximum-width-of-binary-tree/

from leetcode.helper.tree import TreeNode
from collections import deque


class Solution:
    """
        层次遍历即可, 但是如入队时需要将节点编号,且入队规则与
        堆相同, 更根节点序号为 1, 序号为 i 的节点左子树序号
        为 2*i, 右子树序号为 2*i+2
    """
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        ret = 0
        while q:
            left, right = q[0][1], q[-1][1]
            for _ in range(len(q)):
                e, i = q.popleft()
                if e.left:
                    q.append((e.left, i * 2))
                if e.right:
                    q.append((e.right, i * 2 + 1))
            ret = max(ret, right - left + 1)
        return ret
