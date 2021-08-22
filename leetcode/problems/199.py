# 199. 二叉树的右视图
# https://leetcode-cn.com/problems/binary-tree-right-side-view/

from collections import deque
from typing import List

from leetcode.helper.tree import TreeNode


class Solution:
    """
        层次遍历, 取最后一个节点
    """

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                root = queue.popleft()
                root.left and queue.append(root.left)
                root.right and queue.append(root.right)
        return res
