from typing import List

"""
并查集(不相交集) 使用一次 find 的最坏时间复杂度情况是 O(N),
运行时间, 一般情况下, 运行时间是对连续混合使用 M 个指令来计算的,
m 次连续操作在最坏情况下可能花费 O(MN) 时间

灵巧求并算法

1. 按大小求并
合并时, 使得总让较小的树成为较大的树的子树, 我们把这种方法叫做
按大小求并(union-by-size)
比如右两颗树
    a  与   b
          c  d
直接合并可形成
    a
    b
   c d
或
   b
a c  d
按照大小合并可以保证形成第二种情况, 任何节的深度均不会超过 logN
这也就意味着 find 操作的运行时间是 O(logN)
实现: 树根为树大小的负值


2. 按高度求并
跟踪高度而不是大小, union 使得浅的树成为深的树的子树


路径压缩:
路径压缩可以避免求并的最坏的情形
路径压缩在 find 期间执行, 压缩效果为, 从 x 到根的路径上
每一个节点都使他的父节点变成根,路径压缩与按大小求并完全兼容,
也就是两个例程可以同时实现

并查集算法题:
leetcode/problems/547
"""

disjointSet = list(range(100))


def setUnion(root1: int, root2: int, s: List[int]):
    # 直接求并
    s[root2] = root1


def setUnion1(root1: int, root2: int, s: List[int]):
    # 按大小求并
    if s[root1] < s[root2]:
        s[root2] -= s[root1]
        s[root1] = root2
    else:
        s[root1] -= s[root2]
        s[root2] = root1


def setUnion2(root1: int, root2: int, s: List[int]):
    # 按高度求并
    if s[root1] < s[root2]:
        s[root1] = root2
    else:
        if s[root1] == s[root2]:
            s[root1] -= 1
        s[root2] = root1


def find(x: int, s: List[int]):
    # 直接查找, 找到父亲
    if s[x] < 0:
        return x
    return find(s[x], s)


def find1(x: int, s: List[int]):
    # 路径压缩
    if s[x] <= 0:
        return x
    s[x] = find1(s[x], s)
    return s[x]
