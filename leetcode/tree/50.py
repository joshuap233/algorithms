#  二叉树的层序遍历


from typing import List

from tree import generate_tree, TreeNode


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = [[root.val], []]
        layer = 1  # 层次, root节点为第0层
        count = 0  # 当前层已经遍历的节点数
        layer_node_count = 1  # 当前层的节点数
        next_layer_node_count = 0  # 下次节点数
        tree_array = [root]  # 遍历时储存节点
        while tree_array:
            node = tree_array.pop(0)
            if node.left is not None:
                next_layer_node_count += 1
                result[layer].append(node.left.val)
                tree_array.append(node.left)
            if node.right is not None:
                next_layer_node_count += 1
                result[layer].append(node.right.val)
                tree_array.append(node.right)
            count += 1
            # 下一层
            if layer_node_count == count:
                count = 0
                layer_node_count = next_layer_node_count
                next_layer_node_count = 0
                layer += 1
                result.append([])
        # 去除末尾空列表
        end = -1
        for index, item in enumerate(reversed(result)):
            if item:
                break
            end -= 1
        return result[:end + 1]


root = generate_tree([3, 9, 20, None, None, 15, 7])
s = Solution()
print(s.levelOrder(root))
