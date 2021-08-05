# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# 剑指 Offer 52. 两个链表的第一个公共节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# 解题方法与环找第环的入口节点类似
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA, tmpB = headA, headB

        if not (headA and headB):
            return None

        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next if headA else tmpB
            headB = headB.next if headB else tmpA
        return None


# 上面的代码优化
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA, tmpB = headA, headB

        if not (headA and headB):
            return None

        while headA != headB:
            headA = headA.next if headA else tmpB
            headB = headB.next if headB else tmpA
        return headA
