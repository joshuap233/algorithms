from leetcode.helper.link import ListNode


class Solution:
    """做法与 415 题一样"""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = dummy = ListNode(0)
        cur = 0
        while cur or l1 or l2:
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            tail.next = ListNode(cur % 10)
            tail = tail.next
            cur //= 10
        return dummy.next
