# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 19. 删除链表的倒数第 N 个结点

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        双指针,第一个指针先走 n 步,
        递归也行...
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        p1 = p2 = head

        while p1 and n > 0:
            p1 = p1.next
            n -= 1

        prev = None
        while p1:
            prev = p2
            p1 = p1.next
            p2 = p2.next

        if not prev:
            return head.next

        prev.next = prev.next.next
        return head
