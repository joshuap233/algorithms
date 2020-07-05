# 将有序数组转换为二叉搜索树
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def sortedArrayToBST(self, nums: List[int]) -> [TreeNode, None]:
        if not nums:
            return None
        self.generate_binary_search_tree(None, nums)
        return self.root

    def generate_binary_search_tree(self, root: [TreeNode, None], values: list):
        center = (len(values) - 1) // 2
        pre = values[:center + 1]
        las = values[center + 1:]
        if not self.root:
            root = TreeNode(values[center])
            self.root = root
            pre = values[:center]
        if pre:
            node_index = (len(pre) - 1) // 2
            node_value = pre.pop(node_index)
            node = TreeNode(node_value)

            if node_value > root.val:
                root.right = node
            else:
                root.left = node
            self.generate_binary_search_tree(root.left, pre)

        if las:
            node_index = (len(las) - 1) // 2
            node_value = las.pop(node_index)
            node = TreeNode(node_value)
            if node_value > root.val:
                root.right = node
            else:
                root.left = node
            self.generate_binary_search_tree(root.right, las)


# 改进
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> [TreeNode, None]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


s = Solution()
res = s.sortedArrayToBST([-10, -3, 0, 5, 9])
pass
