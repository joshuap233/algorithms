# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        注意这是 二叉搜索树

        设 p.val > q.val

        公共节点有三种情况:
        q.val <=  node <= p.val , node 为公共父节点
        p.val < node.val    公共父节点在 node 左子树
        否则在右子树
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = None
        _min, _max = min(p.val, q.val), max(p.val, q.val)

        def recur(node: TreeNode):
            nonlocal parent
            if not node or parent:
                return
            if _min <= node.val <= _max:
                parent = node
            elif node.val > _max:
                recur(node.left)
            else:
                recur(node.right)

        recur(root)
        return parent


class Solution:
    """
        递归优化为循环
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _min, _max = min(p.val, q.val), max(p.val, q.val)

        while root:
            if _min <= root.val <= _max:
                return root
            elif root.val < _max:
                root = root.right
            else:
                root = root.left
