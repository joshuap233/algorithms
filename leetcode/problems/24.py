# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# 24. 两两交换链表中的节点

from leetcode.helper.link import ListNode


class Solution:
    """解法1,将节点添加到 list"""

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        a = []

        while head:
            a.append(head)
            head = head.next

        for i, v in enumerate(a):
            if i % 2 == 1:
                a[i], a[i - 1] = a[i - 1], a[i]

        head = a[0]
        for i in range(len(a) - 1):
            head.next = a[i + 1]
            head = head.next
        a[-1].next = None
        return a[0]


class Solution1:
    """三指针"""

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        dummy = ListNode(0, head)
        pp = dummy
        p = head
        cur = head.next
        i = 0

        while cur:
            if i % 2 == 0:
                p.next = cur.next
                cur.next = p
                pp.next = cur

                pp = cur
                cur = p.next
            else:
                pp = pp.next
                p = p.next
                cur = cur.next
            i += 1
        return dummy.next
