# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
# 剑指 Offer 35. 复杂链表的复制

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        h = head
        while h:
            nxt = h.next
            h.next = Node(h.val, nxt, h.random)
            h = nxt

        tail = dummy = Node(0)
        while head:
            tail.next = head.next
            tail = tail.next
            if tail.random:
                tail.random = tail.random.next
            head = head.next.next
        return dummy.next

