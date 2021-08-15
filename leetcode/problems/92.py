# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# 92. 反转链表 II
from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        head = dummy

        for _ in range(left - 1):
            head = head.next

        prev = None
        cur = head.next
        for _ in range(left, right + 1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        if head.next:
            head.next.next = cur
        head.next = prev
        return dummy.next


l = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
s.reverseBetween(l, 2, 4)
