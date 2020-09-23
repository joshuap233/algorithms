# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
from typing import List

from leetcode.helper.tree import TreeNode, generate_tree


class Solution:
    def __init__(self):
        self.avg = []

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        self.traverse_tree(root)
        return self.avg

    def traverse_tree(self, root: TreeNode):
        current_layer = [root]
        next_layer = []
        while current_layer or next_layer:
            node_count = len(current_layer)
            count = 0
            while current_layer:
                node = current_layer.pop()
                count += node.val
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            self.avg.append(count / node_count)
            current_layer = next_layer
            next_layer = []


head = generate_tree([3, 9, 20, 15, 7])
s = Solution()
print(s.averageOfLevels(head))
