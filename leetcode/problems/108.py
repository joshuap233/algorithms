# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. 将有序数组转换为二叉搜索树


from typing import List
from leetcode.helper.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node
