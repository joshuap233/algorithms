# 对称二叉树


from tree import generate_tree, TreeNode


# 递归
class Solution:
    def __init__(self):
        self.is_symmetric = True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            self.is_mirror(root.left, root.right)
        return self.is_symmetric

    def is_mirror(self, left_node, right_node):
        if left_node is None and right_node is None:
            return
        if left_node and right_node and left_node.val == right_node.val:
            self.is_mirror(left_node.left, right_node.right)
            self.is_mirror(left_node.right, right_node.left)
        else:
            self.is_symmetric = False
            return


# 迭代
class Solution2:
    def __init__(self):
        self.is_symmetric = True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.is_mirror(root)
        return True

    @staticmethod
    def is_mirror(root) -> bool:
        tree_array = [root.right, root.left]
        while tree_array:
            left = tree_array.pop(0)
            if not tree_array:
                return False
            right = tree_array.pop(0)

            if not left and not right:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            tree_array.append(left.left)
            tree_array.append(right.right)
            tree_array.append(left.right)
            tree_array.append(right.left)
        return True


tree = generate_tree([1, 2, 2, None, 3, None, 3])
s = Solution2()
print(s.isSymmetric(tree))
