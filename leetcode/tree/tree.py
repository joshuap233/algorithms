class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_tree(array: list):
    index = 1
    root = TreeNode(array[0])
    nodes = [root]
    while index < len(array) and nodes:
        node = nodes.pop(0)

        node.left = TreeNode(array[index]) if array[index] is not None else None
        if node.left and node.left.val is not None:
            nodes.append(node.left)
        index += 1

        if index >= len(array):
            continue

        node.right = TreeNode(array[index]) if array[index] is not None else None
        if node.right and node.right.val is not None:
            nodes.append(node.right)
        index += 1

    return root
