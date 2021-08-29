# https://leetcode-cn.com/problems/rotate-list/
# 61. 旋转链表

from leetcode.helper.link import ListNode
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        h1 = h2 = h3 = head
        cnt = 0
        while h3:
            h3 = h3.next
            cnt += 1

        k = k % cnt
        while k > 0:
            h1 = h1.next
            k -= 1

        while h1.next:
            h1 = h1.next
            h2 = h2.next

        h1.next = head
        head = h2.next
        h2.next = None
        return head
