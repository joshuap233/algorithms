from typing import Optional

"""
树的高度: x 节点的高为 x 到树叶的最长路径的长度

1 .AVL 树是其每个节点的左子树和右子树的高度最多差 1 的二叉查找树
2. 通过对树进行简单修正来做到,我们称其为旋转
3. 将必须重新平衡的节点称为 A, 高度不平衡是,有以下四种情况:
   1. 对 A 左儿子的左子树进行一次插入
   2. 对 A 左儿子的右子树进行一次插入
   3. 对 A 右儿子的左子树进行一次插入
   4. 对 A 右儿子的右子树进行一次插入

种类 1,2(N 表示 None):
     A 
  L1    R1
L2  R2  N  N

种类 3,4
     A 
  L1    R1
N  N   L2  R2

可以归类为两种:
a. 插入发生在外边的情形(左-左 或 右-右), 包括 1,4, 需要进行一次单旋转
b. 插入发生在内部的情形(左-右 或 右-左), 包括 2,3, 需要进行一次双旋转 

单旋转:
对于情形 1, 需要将节点 A 降低高度, 可以将 A 的左儿子作为新根:
A 作为 A 左儿子的左子树插入,
而 A 左儿子的右子树(如果存在) 插入到 A ,作为 A 的左子树 (自己画个图更清晰)

旋转前:
      A 
   L1    R1
 L2  R2 
New

旋转后: 
      L1 
  L2       A
New  N   R2   R1


双旋转:
对于情形 2, 先使以 A 左儿子为根用一次右旋转转化为情形 1, 
然后以 A 为根进行一次左旋转

旋转前: 
         A 
   L1       R1
L2    R2  
    NEW
(new 节点也可能是 R2 的右孩子)

右旋转后:
            A 
        R2     R1 
    L1    
L2   NEW


左旋转后:
        R2
    L1      A
L2   NEW       R1        

情形 4 与情形 1 类似, 分别称为右旋转与左旋转,部分文章对左右旋转的定义与这里相反,但方法相同
情形 2 与情形 3 类似 


删除:
  失衡的情况也是上面四种, 不过多了两种特殊情况:
  1. 
           A
     L1        R1
  L2     R2
L3 R3  L4 R4

 2. 
           A
     L1        R1
            L2     R2
           L3 R3  L4 R4
           
这两种情况属于左旋转与右旋转
"""


class Node:
    # 可以添加一个 key 字段, 这里仅使用 val 来查找

    def __init__(
            self, val: int,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None,
            height: int = 0
    ):
        self.val: int = val
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right
        self.height: int = height


class AVLTree:
    """
        增删改查时间复杂度为 O(logN)
    """

    def __init__(self):
        self.root: Optional[Node] = None

    @staticmethod
    def height(node: Optional[Node]):
        return -1 if not node else node.height

    def insert(self, val: int) -> None:
        def Insert(node: Optional[Node]) -> Node:
            if not node:
                return Node(val)

            if val > node.val:
                node.right = Insert(node.right)
            else:
                node.left = Insert(node.left)

            node = self.balance_insert(node, val)
            self.update_height(node)
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

            node = self.balance_delete(node)
            self.update_height(node)
            return node

        self.root = Delete(self.root, val)
        return self.root

    def find(self, val: int) -> Optional[Node]:
        node = self.root
        while node:
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left
            else:
                return node
        return None

    def valid(self) -> bool:
        prev = float('-inf')

        # 验证是否为二叉平衡树
        def Valid(node: Optional[Node]) -> bool:
            nonlocal prev

            if not node:
                return True

            if abs(self.height(node.left) - self.height(node.right)) > 1:
                return False

            if Valid(node.left):
                if node.val < prev:
                    return False
                prev = node.val
                return Valid(node.right)
            return False

        return Valid(self.root)

    def balance_delete(self, node: Node) -> Node:
        ll = self.height(node.left)
        rr = self.height(node.right)

        if ll - rr == 2:
            left = node.left
            if self.height(left.left) - self.height(left.right) >= 0:
                return self.leftRotation(node)
            return self.doubleLeftRotation(node)
        elif rr - ll == 2:
            right = node.right
            if self.height(right.right) - self.height(right.left) >= 0:
                return self.rightRotation(node)
            return self.doubleRightRotation(node)
        return node

    def balance_insert(self, node: Node, val: int) -> Node:
        ll = self.height(node.left)
        rr = self.height(node.right)

        if ll - rr == 2:
            if val < node.left.val:
                return self.leftRotation(node)
            return self.doubleLeftRotation(node)
        elif rr - ll == 2:
            if val < node.right.val:
                return self.doubleRightRotation(node)
            return self.rightRotation(node)
        return node

    def leftRotation(self, node: Node) -> Node:
        # 情形 1
        root = node.left
        right = root.right
        root.right = node
        node.left = right

        self.update_height(node)
        self.update_height(root)
        return root

    def rightRotation(self, node: Node) -> Node:
        # 情形 4
        root = node.right
        left = root.left
        root.left = node
        node.right = left

        self.update_height(node)
        self.update_height(root)
        return root

    def doubleLeftRotation(self, node: Node) -> Node:
        # 情形 2
        node.left = self.rightRotation(node.left)
        return self.leftRotation(node)

    def doubleRightRotation(self, node: Node) -> Node:
        # 情形 3
        node.right = self.leftRotation(node.right)
        return self.rightRotation(node)

    def update_height(self, node: Node):
        if node:
            node.height = max(
                self.height(node.left),
                self.height(node.right)
            ) + 1

    def __bool__(self) -> bool:
        return self.root is not None


if __name__ == '__main__':
    from plot import print_tree
    import random

    tree = AVLTree()

    for i in [1, 3, 4, 5, 6, 7, 8, 2]:
        tree.insert(i)
        print_tree(tree.root)
        assert tree.valid()

    for j in [1, 4, 6]:
        tree.delete(j)
        print_tree(tree.root)
        assert tree.valid()


    def test():
        # 测试插入删除,直接调用即可
        tree = AVLTree()
        for _ in range(10000):
            s = set()
            debug1, debug2 = [], []

            # 随机插入
            for _ in range(20):
                v = random.randint(0, 40)
                while v in s:
                    v = random.randint(0, 40)

                s.add(v)
                debug1.append(v)
                tree.insert(v)
                if not tree.valid():
                    print('debug1: ', debug1)
                    assert False

            # 随机删除
            s = list(s)
            for _ in range(20):
                v = random.choice(s)
                s.remove(v)

                debug2.append(v)
                tree.delete(v)
                if not tree.valid():
                    print('debug1: ', debug1)
                    print('debug2: ', debug2)
                    assert False
