# 验证二叉搜索树
# 节点的左子树"只"包含"小于当前节点"的数。
# 节点的右子树"只"包含"大于当前节点"的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
from tree import generate_tree


class Solution:
    def __init__(self):
        self.is_valid_bst = True
        self.tree_array = []

    def isValidBST(self, root) -> bool:
        if root:
            self.inorder_traversal(root)
        for index, node in enumerate(self.tree_array[1:]):
            if self.tree_array[index].val >= node.val:
                self.is_valid_bst = False
                break
        return self.is_valid_bst

    # 中序遍历为严格递增,则为搜索二叉树
    def inorder_traversal(self, node):
        if node.left is None:
            self.tree_array.append(node)
        else:
            self.inorder_traversal(node.left)

        # 防止node被重复添加
        if node.left is not None:
            self.tree_array.append(node)

        if node.right is not None:
            self.inorder_traversal(node.right)


root = generate_tree([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])
s = Solution()
print(s.isValidBST(root))
