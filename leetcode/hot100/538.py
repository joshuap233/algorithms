# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 538. 把二叉搜索树转换为累加树

# 类似的题:
# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 98. 验证二叉搜索树

from leetcode.helper.tree import TreeNode


class Solution:
    """
        树中的所有值 互不相同 。
        给定的树为二叉搜索树。

        使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

        改下中序遍历即可,中序遍历:
            recur(node.left)
                在这里可以从小到大访问节点
            recur(node.right)

        现在改成
            recur(node.right)
                在这里可以从大到小访问节点
            recur(node.left)

        Sum = 0 相当于 prev
    """

    def convertBST(self, root: TreeNode) -> TreeNode:
        Sum = 0

        def recur(node: TreeNode):
            nonlocal Sum
            if not node:
                return

            recur(node.right)

            Sum = Sum + node.val
            node.val = Sum

            recur(node.left)

        recur(root)
        return root
