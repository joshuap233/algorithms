# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/

from typing import List

from leetcode.tree.tree import TreeNode, generate_tree


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.traversal(root)
        return self.res

    def traversal(self, node: TreeNode):
        if node is None:
            return
        self.traversal(node.left)
        self.res.append(node.val)
        self.traversal(node.right)


head = generate_tree([1, None, 2, 3])
s = Solution()
print(s.inorderTraversal(head))
