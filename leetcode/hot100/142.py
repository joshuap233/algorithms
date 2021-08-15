# https://leetcode-cn.com/problems/linked-list-cycle-ii/
# 142. 环形链表 II
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        # 判断是否有环
        slow, fast = head, head
        while True:
            if not (slow and fast and fast.next):
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        first = head
        while first != slow:
            first = first.next
            slow = slow.next

        return first
