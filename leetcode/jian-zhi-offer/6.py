# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
# 剑指 Offer 06. 从尾到头打印链表

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        v = []
        while head is not None:
            v.append(head.val)
            head = head.next
        v.reverse()
        return v
