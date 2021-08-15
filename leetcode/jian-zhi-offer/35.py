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
            return None

        tmp = head
        while head:
            new = Node(head.val, head.next, head.random)
            _next = head.next
            head.next = new
            head = _next

        head = tmp
        while head:
            node = head.next
            _next = node.next

            node.random = head.random.next if head.random else None
            node.next = _next.next if _next else None
            head = _next

        return tmp.next
