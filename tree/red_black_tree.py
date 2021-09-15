from typing import Optional, List

# 打印红黑树
import networkx as nx
import matplotlib.pyplot as plt

"""
    红黑树是 AVL 树的一种变种,对红黑树操作在最坏的情况下
    花费 O(logN) 时间, 对于插入操作,一种非递归实现可以相对容易地完成(与 AVL 树相比)

    红黑树的性质:
    1. 每个节点或者红色或者黑色
    2. 根是黑色
    3. 如果一个节点是红色, 那么它的子节点必须是黑色
    4. 从一个节点到 NULL 指针的每一条路径必须包含相同数目的黑色节点
    约定: NULL 节点为黑色(这个约定似乎除了增加理解的难度之外没有用处?)
    
    这些约束确保了红黑树的关键特性：从根到叶子的最长的可能路径不多于
    最短的可能路径的两倍长 (因为第四条约束, 红黑树不能一直朝一个方向延伸
    ,如果红黑树一直朝一个方向延伸, 那么根节点到 NULL 指针的黑色节点数目必然不同
    ,除新节点都为红色节点, 但第三条约束保证不能有连续的红节点)
    
    着色法则的一个推论是, 红黑树的高度最多是 2log(N+1), 因此保证
    查找是一种对数的操作(证明见 WIKI)
    
    红黑树叶子节点有下面两种情况:
    1. 
        黑
      红  红  
    红节点的子节点个数为 [0,2]
    
    2.  ?
     黑    黑
     
插入有两种方案: 
    1. 插入黑色放到树叶中, 情形 1,2 都会与红黑树着色规则冲突,也就是插入一次需要调整一次
    2. 插入红色放到树叶中, 父节点是红色的情况需要调整(旋转,重新着色)
    选择方案 2
    
    
插入的情况:
1. 父节点为黑色, 直接插入

=============
2. 父节点为红色, 叔父节点不存在(或为黑色),当 new 为新节点时, 黑色叔父节点必然不存在, 
当 new 上滤(情形3)过程中变色的节点时, 叔父节点可以为黑色

2.1.1 插入父节点左边(N 为新节点):

      黑(G)
   红(P)          
红(N)


左旋转后 -> :


    黑(p)
红(N)   红(G)

=============
2.1.2 插入父节点左边(N 为上滤变色的节点)
      黑(G)
   红(P)     R1       
红(N)  R2

左旋转后 -> : 
    
    黑(p)
红(N)   红(G)
       R2   R1

可以发现 2.1.1 就是 2.1.2 的一种情况
=============
2.2.1 插入父节点右边(N 为新节点):
      黑(G)
   红(P)             
     红(N)

以 P 节点为根进行右旋转 ->:
      黑(G)
   红(N)           
红(P)

回到了情况 2.1.1, 再次进行左旋转即可


=============
2.2.1 插入父节点右边(N 为上滤变色的节点):
        黑(G)
   红(P)       R1         
R2    红(N)

以 P 节点为根进行右旋转 ->:
              黑(G)
         红(N)      R1      
    红(P)
 R2

现在回到了情况 2, 再次进行左旋转 ->:
    
         黑(N)
  红(P)         红(G)
R2    R1            R1

可以发现 2.2.1 就是 2.2.2 的一种情况
=============
3. 父节点为红色, 叔父节点为红色
        黑(G)
    红(P)    红(S)
红(NEW)

三个红色节点,一个黑色节点,
必需将根涂成红色来保证符合红黑树特性, 根变成红色,如果根的父节点
为红色,那么需要上滤,直到没有两个连续红色节点

-> 

        红(G)
    黑(P)    黑(S)
红(NEW)

上滤过程中,可能会遇到情况 2, 也可能遇到情况 3

上面是自底向上插入过程(递归)

自顶向下插入:
查找过程中,遇到一个节点 x 有两个红儿子, 那么将 x 成为红,
他的两个儿子重绘成黑, 如果 x 的父节点 p 也为红,那么会破坏红黑树约定,
需要进行上面的旋转(p 的兄弟节点不可能是红色, 自顶向上的插入会保证搜索
路径中不存在两个红色兄弟节点)
这种插入旋转之后会让上层产生 2 个红色节点,但可以保证插入点不存在叔父节点与父节点都为红色的情况
比如:
     黑(x)
  红      红

->   红(x)
    黑   黑
  
->  
     红(p)     
红(x)    黑()

-> 
   黑
红     红


经验指出,平均红黑树大约和平均 AVL 树一样深,从而查找时间接近最优,红黑树的优点是执行插入所需要的开销相对
较低, 再有就是实践中发生的旋转相对较少

以前 linux 的红黑树有指向 parent 的指针,
现在(5.15 版本) 没有 parent 的指针,但是有一个__rb_parent_color 字段(unsigned long),
记录父节点地址与当前节点颜色, 父节点使用宏找到:
#define rb_parent(r)   ((struct rb_node *)((r)->__rb_parent_color & ~3))
这应该是把颜色和地址存到一起了,分配节点的时候 8 字节对齐,颜色存低三位

参考:
https://github.com/skywind3000/avlmini/blob/master/test/linux_rbtree.c
https://github.com/torvalds/linux/blob/5bfc75d92efd494db37f5c4c173d3639d4772966/tools/include/linux/rbtree.h
"""


class Node:
    # 可以添加一个 key 字段, 这里仅使用 val 来查找
    def __init__(
            self, val: int,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None,
            parent: Optional['Node'] = None,
            red: bool = True
    ):
        self.val: int = val
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right
        # 书上的实现没有这个指针,因此自顶向下的实现遇到有两个
        # 红色儿子的节点就需要重新上色与旋转,而添加该指针后,
        # 可以迭代达到底部插入,然后上滤
        self.parent: Optional['Node'] = parent
        self.red: bool = red


class RBTree:
    def __init__(self):
        # 所有节点共享的空节点,减少边界判断
        self.NULL = Node(-1, red=False)
        self.NULL.left = self.NULL
        self.NULL.right = self.NULL

        # 哑节点, 添加哑节点好像没什么用,而且打印函数还需要修改
        self.root: Optional[Node] = None

    def insert(self, val: int):
        new = Node(val, self.NULL, self.NULL, red=True)
        parent = root = self.root
        if not self.root:
            new.red = False
            self.root = new
            return

        # parent 为可插入的节点
        while root != self.NULL:
            parent = root
            if val < root.val:
                root = root.left
            else:
                root = root.right

        new.parent = parent
        if new.val > parent.val:
            parent.right = new
        else:
            parent.left = new

        if not parent.red:
            return

        self.balance_insert(new)

    def balance_insert(self, node: Node):
        item = node.val  # 用来简化算法
        while node != self.root and node.parent.red:
            p = node.parent
            gp = p.parent
            if not (gp.left.red and gp.right.red):
                gp.red = True
                if p.val < gp.val:
                    p.red = False
                else:
                    node.red = False

                if p.val < item < gp.val or gp.val < item < p.val:
                    self.rotate(gp, item)  # 双旋转
                self.rotate(gp.parent, item)
                # 旋转过后,新根必然为黑色
                break
            gp.left.red = gp.right.red = False
            gp.red = True
            node = node.parent.parent
        self.root.red = False

    def rotate(self, parent: Node, item: int):
        if not parent:
            self.root = self.leftRotation(self.root) \
                if item < self.root.val else self.rightRotation(self.root)
            return

        if item < parent.val:
            parent.left = self.leftRotation(parent.left) \
                if item < parent.left.val else self.rightRotation(parent.left)
            parent.left.parent = parent
            return

        parent.right = self.leftRotation(parent.right) \
            if item < parent.right.val else self.rightRotation(parent.right)
        parent.right.parent = parent

    @staticmethod
    def leftRotation(node: Node) -> Node:
        root = node.left
        right = root.right

        root.right = node
        node.parent = root

        node.left = right
        return root

    @staticmethod
    def rightRotation(node: Node) -> Node:
        root = node.right
        left = root.left

        root.left = node
        node.parent = root

        node.right = left
        return root

    def balance_delete(self):
        pass

    def delete(self, val: int):
        pass

    def find(self, val: int) -> Optional[Node]:
        root = self.root
        while root and root.val != val:
            if val > root.val:
                root = root.right
            else:
                root = root.left
        return root

    def valid(self) -> bool:
        def Valid(node: Node) -> int:
            nonlocal v
            if node == self.NULL or not v:
                return 0

            if node.red and node.parent.red:
                v = False
                return 0

            left = Valid(node.left)
            right = Valid(node.right)
            if left != right:
                v = False
                return 0
            return left + (0 if node.red else 1)

        v = True
        Valid(self.root.right)
        return v

    def __bool__(self) -> bool:
        return self.root is not None

    def print(self):
        def create_graph(node, x=0, y=0, layer: int = 1) -> None:
            pos[node.val] = (x, y)
            color_map.append("red" if node.red else "black")
            if node.left != self.NULL:
                g.add_edge(node.val, node.left.val)
                l_x = x - 1 / (2 ** layer)
                create_graph(node.left, l_x, y - 1, layer + 1)

            if node.right != self.NULL:
                g.add_edge(node.val, node.right.val)
                r_x = x + 1 / (2 ** layer)
                create_graph(node.right, r_x, y - 1, layer + 1)

        if not self.NULL:
            print("空树")
            return

        g = nx.DiGraph()
        pos = {}
        color_map = []
        create_graph(self.root)
        fig, ax = plt.subplots(figsize=(8, 10))
        nx.draw_networkx(
            g,
            pos,
            ax=ax,
            node_size=300,
            font_size=10,
            font_color="#fff",
            node_color=color_map,
            arrows=False
        )
        plt.show()


if __name__ == '__main__':
    import random

    tree = RBTree()
    for i in [34, 8, 13, 23, 30, 19, 0, 22]:
        tree.insert(i)
        tree.print()
        assert tree.valid()


    def test():
        # 测试插入删除,直接调用即可
        tree = RBTree()
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
        print("PASS")
    # test()
