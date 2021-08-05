# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# 剑指 Offer 22. 链表中倒数第k个节点

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        hdr, hdr1 = head, head
        while hdr and k > 0:
            hdr = hdr.next
            k -= 1

        if k > 0:
            return None

        while hdr:
            hdr = hdr.next
            hdr1 = hdr1.next
        return hdr1
