# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# 92. 反转链表 II
from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        tail = dummy = ListNode(0, head)

        for i in range(left - 1):
            tail = tail.next

        prev = None
        tmp = h = tail.next
        for _ in range(left, right + 1):
            nxt = h.next
            h.next = prev
            prev = h
            h = nxt
        tail.next = prev
        tmp.next = h
        return dummy.next


l = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
s.reverseBetween(l, 2, 4)
