# https://leetcode-cn.com/problems/add-two-numbers-ii/
# 445. 两数相加 II

from leetcode.helper.link import ListNode, generate_link_list
from collections import deque


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getVal(head: ListNode) -> str:
            v = ''
            while head:
                v = v + str(head.val)
                head = head.next
            return v

        s = str(int(getVal(l1)) + int(getVal(l2)))
        p = 0
        dummy = tail = ListNode(0)
        while p < len(s):
            tail.next = ListNode(int(s[p]))
            tail = tail.next
            p += 1
        return dummy.next


class Solution1:
    """
        进阶：如果输入链表不能修改该如何处理？换句话说，
        不能对列表中的节点进行翻转。
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = deque()
        stack2 = deque()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        cur = 0
        nxt = None
        while cur or stack1 or stack2:
            if stack1:
                cur += stack1.pop()
            if stack2:
                cur += stack2.pop()
            node = ListNode(cur % 10)
            node.next = nxt
            nxt = node
            cur //= 10
        return nxt
