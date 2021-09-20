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



1. 删除的节点有两个儿子, 那么转化为删除只有一个儿子的情况(找到左
子树最大值或右子树最小值代替当前节点), 实际删除的节点必然最多只有一个儿子,
因为当需要删除的节点有两个儿子时,会查找左子树最大值或右子树最小值代替
需要删除的节点, 找到的节点最多只有一个儿子, 如果两个儿子都不存在, 
那么将任意一个空节点当成儿子即可


2. 删除的节点只有一个儿子(如果左右都是空指针, 那么选择任意一个空作为儿子即可)
2.1 被删除的节点为红, 直接删除, 子节点代替当前节点
2.2 被删除的节点为黑, 子节点为红,直接删除, 子节点代替当前节点,涂黑
2.3 被删除的节点 A 为黑, 子节点为黑,这种情况下 A 必然为叶子, 左右儿子都指向
NULL(黑色), 因为 A 最多只有一个儿子, 如果他的这个儿子为黑,那么左右儿子的黑色节点
数不等,违反红黑树规则

设 n 是替代删除节点的节点,原节点已经被删除, s 为 n 的兄弟节点

2.3.1 n 为新根, 结束
两种情况, 一种只剩 n ,一种在上滤过程中,需要平衡的节点达到根,比如 2.3.3
  
  
2.3.2  s 为红色
     p(黑)
n(黑)      s(红)
         sl    sr
        
-> 对 p 进行右旋转, p, s 交换颜色

        s(黑)
    p(红)      sr
 n(黑)  sl
 
然后按照  2.3.4 处理
 
2.3.3 p,s,sl,sr 都为黑
     p(黑)
n(黑)     s(黑)
        sl   sr
        
-> 将 s 重绘为红色
     p(黑)
n(黑)     s(红)
        sl    sr

通过 S 的所有路径，都少了一个黑色节点。
因为删除 N 的初始的父亲使通过 N 的所有路径少了一个黑色节点,所以 p 节点
以及 p 的子节点都达到了平衡, 但是, 通过 p 与 不通过 p 节点的路径相差
一个黑色节点, 所以需要对 p 进行重新平衡.从情形 2.3.1 开始向下考虑


2.3.4 s 和 s 的儿子都是黑色,但 P 是红色
         p(红)
    N(黑)     s(黑)
            sl    sr
    
-> 交换 p, s 的颜色

     p(黑)
N(黑)     s(红)
        sl    sr
    
结束, 通过 p 与不通过 p 的黑色节点数相同


2.3.5  s 为黑, s 左儿子或右儿子为红
左儿子为红(双旋转):

         s(黑)
    sl(红)   sr(黑)

-> 对 s 左旋转, sl, s 交换颜色

        sl(黑)
             s(红)
                 sr(黑)
                 
进入右儿子为红的状态:      

      p(?)
n(黑)     s(黑)
            sr(红)

-> 对 p 做右旋转, sr 涂黑, p,s 交换颜色
    
      s(?)
  p(黑)   sr(黑)
n(黑)     



总的来说分为以下几种:
1. n 为根  (结束)
2. p 为红  (结束)
3. s 的儿子为红(单旋转或双旋转, 结束)

4. 所有节点为黑 s 涂红, 变成 s 为红的情况, 此时 p 的左边路径和右边路径
都缺少了一个黑色节点, 因此需要回溯到父亲节点,继续修复

5. s 为红   (旋转成 p 为红的情况)
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

        # root 使用哑节点好像没什么用,而且打印函数还需要修改
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

        self.balanceInsert(new)

    def balanceInsert(self, node: Node):
        while node != self.root and node.parent.red:
            p = node.parent
            gp = p.parent
            if not (gp.left.red and gp.right.red):
                if p == p.parent.left:
                    # 左右双旋转
                    if node == p.right:
                        node = node.parent
                        self.rightRotation(node)  # 双旋转
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.leftRotation(node.parent.parent)
                else:
                    # 右左双旋转
                    if node == p.left:
                        node = node.parent
                        self.leftRotation(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rightRotation(node.parent.parent)
                break
            gp.left.red = gp.right.red = False
            gp.red = True
            node = node.parent.parent
        # 新根为黑
        self.root.red = False

    def leftRotation(self, node: Node) -> Node:
        root = node.left
        right = root.right

        root.right = node
        root.parent = node.parent

        if node == self.root:
            self.root = root
        elif node == node.parent.right:
            node.parent.right = root
        else:
            node.parent.left = root
        node.parent = root
        node.left = right
        right.parent = node
        return root

    def rightRotation(self, node: Node) -> Node:
        root = node.right
        left = root.left

        root.left = node
        root.parent = node.parent

        if node == self.root:
            self.root = root
        elif node == node.parent.right:
            node.parent.right = root
        else:
            node.parent.left = root

        node.parent = root
        node.right = left
        left.parent = node
        return root

    def balanceDelete(self, node: Node):
        # node 为代替删除节点位置的节点
        while node != self.root and not node.red:
            p = node.parent
            s = p.right if node == p.left else p.left

            # p, s ,sl,sr 为黑色
            if not (p.red or s.red or s.left.red or s.right.red):
                s.red = True
                node = node.parent
                continue

            # p 为红色
            if p.red and not (s.left.red or s.right.red):
                node = p
                s.red = True
                break

            if node == p.left:
                if s.red:
                    p.red, s.red = True, False
                    self.rightRotation(p)
                    s = p.right

                if s.left.red or s.right.red:
                    # s 右儿子为黑
                    if not s.right.red:
                        s.red, s.left.red = True, False
                        self.leftRotation(s)
                        s = p.right
                    # 左右儿子都为红或左儿子为黑
                    s.right.red = False
                    p.red, s.red = s.red, p.red
                    self.rightRotation(p)
                    break
            else:
                if s.red:
                    p.red, s.red = True, False
                    self.leftRotation(p)
                    s = p.left

                if s.left.red or s.right.red:
                    if not s.left.red:
                        s.red, s.right.red = True, False
                        self.rightRotation(s)
                        s = p.left
                    s.left.red = False
                    p.red, s.red = s.red, p.red
                    self.leftRotation(p)
                    break
        node.red = False

    def delete(self, val: int) -> bool:
        d = self.root
        while d != self.NULL and d.val != val:
            if d.val < val:
                d = d.right
            else:
                d = d.left
        if d == self.NULL:
            return False

        if d.left == self.NULL:
            x = d.right
            self._delete(d, d.right)
        elif d.right == self.NULL:
            x = d.left
            self._delete(d, d.left)
        else:
            tmp = d
            d = self.mini(d.right)
            x = d.right
            self.copyNode(d, tmp)
            self._delete(d, x)

        # 删除红色节点不需要重新平衡
        # d 为实际删除的节点, x 为代替 d 位置的节点(可能为 NULL)
        if not d.red:
            if x.red:
                x.red = False
                return True
            self.balanceDelete(x)
        return True

    @staticmethod
    def copyNode(src: Node, dest: Node):
        dest.val = src.val

    def mini(self, node: Node):
        while node.left != self.NULL:
            node = node.left
        return node

    def _delete(self, parent: Node, son: Node):
        # parent 为需要删除的节点, son 为代替 parent 的儿子节点
        if parent.parent is None:
            self.root = son
        elif parent == parent.parent.left:
            parent.parent.left = son
        else:
            parent.parent.right = son
        son.parent = parent.parent

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
            nonlocal v, prev
            if node == self.NULL or not v:
                return 0

            if node.red and node.parent.red:
                v = False
                return 0

            left = Valid(node.left)
            if node.val < prev:
                v = False
                return 0
            prev = node.val
            right = Valid(node.right)
            if left != right:
                v = False
                return 0
            return left + (0 if node.red else 1)

        prev = float('-inf')
        v = True
        Valid(self.root)
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


    def test():
        # 测试插入删除,直接调用即可
        for i in range(10000):
            tree = RBTree()
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
                if not (tree.delete(v) and tree.valid()):
                    print('debug1: ', debug1)
                    print('debug2: ', debug2)
                    assert False

        print("PASS")


    def debug():
        tree = RBTree()
        for i in [27, 22, 3, 32, 26, 31, 20, 28, 36, 8, 13, 11, 24, 15, 33, 37, 6, 17, 7, 16]:
            tree.insert(i)
            assert tree.valid()

        tree.print()
        for i in [33, 32, 28, 20]:
            if i == 20:
                print(1)
            assert tree.delete(i)
            tree.print()
            print(i)
            assert tree.valid()


    # test()
    debug()
