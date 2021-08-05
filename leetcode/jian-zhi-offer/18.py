# https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
# 剑指 Offer 18. 删除链表的节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        tmp = head
        prev = head
        while head:
            if head.val == val:
                prev.next = head.next
                break
            prev = head
            head = head.next
        return tmp

