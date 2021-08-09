# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# 124. 二叉树中的最大路径和
from typing import List

from leetcode.helper.tree import TreeNode


class Solution:
    """
        返回长度为 2 的数组 a
        a[0] 为:
             cur
            /
           /
        形式的路径和

        a[1] 为
          cur
         /
        /\
        形式的路径和,也就是, cur 还可以与 a[0] 相加,
        但 a[1] 不可以与 cur 相加
        上面的方法给爷整不会了...每次都还有几个样例通不过....
        而且组合方式很多...

         对于任意一个节点, 如果最大和路径包含该节点, 那么只可能是两种情况:
        1. 其左右子树中所构成的和路径值较大的那个加上该节点的值后向父节点回溯构成最大路径
        2. 左右子树都在最大路径中, 加上该节点的值构成了最终的最大路径

        返回左右子树中较大的那个 + 当前值即可,不过每层递归需要记录最大值
        利用回溯计算第 1 点的值, 当前递归返回计算第二点的值
    """

    def maxPathSum(self, root: TreeNode) -> int:
        maxi = root.val

        def recur(node: TreeNode) -> int:
            nonlocal maxi
            if not node:
                return 0

            left = max(0, recur(node.left))
            right = max(0, recur(node.right))
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val

        recur(root)
        return maxi
