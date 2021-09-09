# https://leetcode-cn.com/problems/path-sum/
# 112. 路径总和
from typing import Optional
from leetcode.helper.tree import TreeNode


class Solution:
    """
        一写就错,服了...
        注意
           1
         /
       2
       在遇到 root 节点为 None 是判断 s 是否满足要求并不合适, 因为
       该节点不一定是叶子
    """

    def hasPathSum(self, root: Optional[TreeNode], s: int) -> bool:
        if not root:
            return False

        s -= root.val
        if not (root.left or root.right):
            if s == 0:
                return True
            return False
        return self.hasPathSum(root.left, s) or self.hasPathSum(root.right, s)

