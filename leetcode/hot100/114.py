# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# 114. 二叉树展开为链表

# 和下面的题目有点像
# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 98. 验证二叉搜索树


from leetcode.helper.tree import TreeNode, generate_tree
from typing import Optional


class Solution:
    """
        进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

        也就是递归也不能用, 用栈模拟也不会是 O(1) 空间啊???

        所以需要有个 prev 指针,或者用二叉树而右子树存储之前的节点,
        但二叉树的右子树不是空怎么办?

        我的想法,首先找到左子树最左边的节点,
        遍历过程中,如果当前节点 a 的右子树存在,则将 a 的最右节点
        连接到上一个节点(即 a 的父节点的右孩子或 a 的父节点的父节点的....)

        下面的解法和上面的想法差不多,就是一直找左子树,然后将右子树最右节点连接到
        上一个节点(即 a 的父节点的右孩子或 a 的父节点的父节点的....)
    """

    def flatten(self, root: TreeNode) -> None:
        while root:
            # 对当前节点左子树操作,(否则需要存取
            # prev,然后对前面的节点操作)
            if root.left:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


class Solution1:
    """
        递归算法,很明显不是原地算法
        前序遍历,在 recur(node.left) 前设置 prev 即可
    """

    def flatten(self, root: TreeNode) -> None:
        prev = None

        def recur(node: TreeNode):
            nonlocal prev

            if not node:
                return

            right = node.right
            if prev:
                prev.right = node
            prev = node

            recur(node.left)
            node.left = None
            recur(right)

        recur(root)
