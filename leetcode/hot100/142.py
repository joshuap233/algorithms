# https://leetcode-cn.com/problems/linked-list-cycle-ii/
# 142. 环形链表 II
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
        使用快慢双指针
        设非环部分长 a, 环部分长 b
        双指针向相遇时,
        fast 指针走了 f 步, slow 指针走了 s 步
        f = 2*s
        s = a + n*b
        s = nb 也就是说 s 再走 a 步就到环入口点了,
        这时候设置第三个指针从 head 开始,直到与slow 指针相遇

        你是否可以使用 O(1) 空间解决此题？
        说明：不允许修改给定的链表。
    """

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
