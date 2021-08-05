# https://leetcode-cn.com/problems/add-two-numbers/
# 2. 两数相加

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        of = 0
        head, tail = None, None
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + of
            else:
                val = (l1 or l2).val + of
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            of = val // 10
            val = val % 10
            node = ListNode(val, None)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node

        if of == 1:
            tail.next = ListNode(1, None)
        return head
