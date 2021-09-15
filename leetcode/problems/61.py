# https://leetcode-cn.com/problems/rotate-list/
# 61. 旋转链表

from leetcode.helper.link import ListNode
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        le = 0
        h = head
        while h:
            le += 1
            h = h.next
        k %= le
        p1 = p2 = head
        for _ in range(k):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = head
        ret = p2.next
        p2.next = None
        return ret
