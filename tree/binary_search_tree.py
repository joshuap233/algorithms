from typing import Optional

"""
最麻烦的删除操作:
    需要删除的节点为 A
    1. A 为树叶,直接删除
    2. A 只有一个儿子, 儿子代替父节点即可
    3. A 有两个儿子, 找到 A 右子树中最小的节点删除, 然后代替 A 

测试(偷懒用 leetcode 测试):
    查找: leetcode T700
    插入: leetcode T701
    删除: leetcode T450
    验证: leetocde T98
"""


class Node:
    # 可以添加一个 key 字段, 这里仅使用 val 来查找

    def __init__(
            self, val: int,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None
    ):
        self.val: int = val
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right


class BSTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, val: int) -> None:
        def Insert(node: Optional[Node]) -> Node:
            if not node:
                return Node(val)

            if val > node.val:
                node.right = Insert(node.right)
            else:
                node.left = Insert(node.left)
            return node

        self.root = Insert(self.root)

    def delete(self, val: int) -> None:
        def findMin(node: Node) -> int:
            while node.left:
                node = node.left
            return node.val

        def Delete(node: Optional[Node], target: int) -> Optional[Node]:
            if not node:
                return node

            if target > node.val:
                node.right = Delete(node.right, target)
            elif target < node.val:
                node.left = Delete(node.left, target)
            else:
                if not (node.left and node.right):
                    return node.left or node.right
                node.val = findMin(node.right)
                node.right = Delete(node.right, node.val)
            return node

        self.root = Delete(self.root, val)
        return self.root

    def find(self, val: int) -> Node:
        def Find(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None
            if node.val == val:
                return node
            return Find(node.left) \
                if val < node.val else Find(node.right)

        return Find(self.root)

    def valid(self):
        # 验证是否为二叉搜索树
        prev = float('-inf')

        def Valid(node: Node) -> bool:
            if not node:
                return True

            nonlocal prev
            if Valid(node.left):
                if node.val < prev:
                    return False
                prev = node.val
                return Valid(node.right)
            return False

        return Valid(self.root)

    def __bool__(self) -> bool:
        return self.root is not None


if __name__ == '__main__':
    from plot import print_tree
    from random import randint

    tree = BSTree()
    for i in range(10):
        new = randint(0, 20)
        while tree.find(new):
            new = randint(0, 20)
        tree.insert(new)
        assert tree.valid()

    print_tree(tree.root)
