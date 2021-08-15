# https://leetcode-cn.com/problems/reorder-list/
# 143. 重排链表

from leetcode.helper.link import ListNode, generate_link_list
from collections import deque


class Solution:
    """
        解法1, 把节点存到 list 中即可
    """

    def reorderList(self, head: ListNode) -> None:
        a = []
        h = head
        while h:
            a.append(h)
            h = h.next
        n = len(a)

        for i in range(n // 2):
            Next = head.next
            head.next = a[-i - 1]
            a[-i - 1].next = Next
            head = Next

        a[n // 2].next = None
        if n % 2 == 1 and n > 1:
            a[n // 2 + 1].next = a[n // 2]


hdr = generate_link_list([1, 2, 3, 4])
s = Solution()
s.reorderList(hdr)
