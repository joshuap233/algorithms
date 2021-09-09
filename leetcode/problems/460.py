# https://leetcode-cn.com/problems/lfu-cache/
# 460. LFU 缓存
from typing import Dict


class Node:
    # 双向链表
    def __init__(
            self,
            value: int = 0,
            key: int = 0,
            cnt: int = 1,

            n: 'Node' = None,
            p: 'Node' = None,

            h: 'Node' = None,  # 指向 head
            nh: 'Node' = None,  # 每层头节点存在, 指向下一个头结点
            ph: 'Node' = None  # 每层头节点存在, 指向上一个头结点
    ):
        self.value = value
        self.cnt = cnt
        self.key = key

        self.next = n or self
        self.prev = p or self
        self.head = h or self

        self.next_head = nh
        self.prev_head = ph


class LFUCache:
    """
        进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？

        链表结构(head 节点不包含数据):
        同层节点次数相同, 且包含一个指向 head 的指针

        dummyHead
          |
        head1 -> n1-> n2 -> head1 (双向链表)
         |
        head2 -> n3 -> n4 ...
         |
        head3
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: Dict[int, Node] = {}
        self.dummy = Node(cnt=0)
        self.dummy.prev_head = self.dummy
        self.dummy.next_head = self.dummy

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        n = self.map[key]
        n.cnt += 1
        head = n.head
        self.delete(n)
        self.insert(n, head)
        return n.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.map:
            node = self.map[key]
            node.value = value
            node.cnt += 1
            self.delete(node)
            self.insert(node, node.head)
        else:
            if len(self.map) == self.cap:
                e = self.dummy.next_head.next
                self.delete(e)
                del self.map[e.key]
            node = Node(key=key, value=value)
            self.insert(node, self.dummy)
            self.map[key] = node

    def insert(self, node: Node, head: Node):
        cur_head = head.next_head
        if cur_head.cnt != node.cnt:
            # 新增 head
            cur_head = Node(cnt=node.cnt)
            self.insert_head(head, cur_head)

        # 新节点插入头结点尾部
        node.prev = cur_head.prev
        node.next = cur_head
        cur_head.prev.next = node
        cur_head.prev = node
        node.head = cur_head

    def delete(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        head = node.head
        if head.next == head:
            self.delete_head(head)
            
    @staticmethod
    def delete_head(cur: Node):
        cur.next_head.prev_head = cur.prev_head
        cur.prev_head.next_head = cur.next_head

    @staticmethod
    def insert_head(prev: Node, cur: Node):
        cur.prev_head = prev
        cur.next_head = prev.next_head

        prev.next_head.prev_head = cur
        prev.next_head = cur


s = LFUCache(1)
a = ["put", "get", "put", "get", "get"]
b = [[2, 1], [2], [3, 2], [2], [3]]

for i, v in enumerate(a):
    vb = b[i]
    if v == 'put':
        s.put(vb[0], vb[1])
    else:
        print(s.get(vb[0]))
