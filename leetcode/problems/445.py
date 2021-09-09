# https://leetcode-cn.com/problems/add-two-numbers-ii/
# 445. 两数相加 II

from leetcode.helper.link import ListNode, generate_link_list


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


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r1 = r2 = ''
        while l1:
            r1 = str(l1.val) + r1
            l1 = l1.next

        while l2:
            r2 = str(l2.val) + r2
            l2 = l2.next

        v = str(int(r1) + int(r2))
        p = len(v) - 1
        dummy = tail = ListNode(0)
        while p >= 0:
            tail.next = ListNode(int(v[p]))
            tail = tail.next
            p -= 1
        return dummy.next


class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        head = tail = ListNode(0)
        while l1 or l2:
            val = l1.val if l1 else 0
            val += l2.val if l2 else 0
            val += overflow

            overflow = val // 10
            val = val % 10

            l1 = l1 and l1.next
            l2 = l2 and l2.next

            node = ListNode(val, None)
            tail.next = node
            tail = node

        if overflow == 1:
            tail.next = ListNode(1, None)
        return head.next
