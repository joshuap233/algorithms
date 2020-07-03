# 对称二叉树


from tree import generate_tree, TreeNode


# 迭代
class Solution:
    def __init__(self):
        self.tree_value = []
        self.temp = []
        self.is_symmetric = True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            self.temp.append(root)
            self.level_traversal()
            return self.is_symmetric

    # 层次遍历
    def level_traversal(self):
        # 节点数量 用于判断该层是否遍历完成
        count = 0
        layer = 0
        while self.temp:
            node = self.temp.pop(0)
            if node.left:
                self.temp.append(node.left)
                self.tree_value.append(node.left.val)
            if node.right:
                self.temp.append(node.right)
                self.tree_value.append(node.right.val)
            count += 1
            if (2 ** layer) == count:
                if not self.array_is_symmetrical(self.tree_value):
                    self.is_symmetric = False
                    return
                layer += 1
                count = 0
                self.tree_value.clear()

    @staticmethod
    def array_is_symmetrical(array):
        for i in range(len(array) // 2):
            if array[i] != array[-(i + 1)]:
                return False
        return True


tree = generate_tree([1, 2, 2, 3, 4, 4, 3])
s = Solution()
print(s.isSymmetric(tree))
