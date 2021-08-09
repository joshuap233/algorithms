# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# 23. 合并K个升序链表

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        将所有节点添加到一个新 list 中,排序连接即可
        理论上 nlongn,实际上 Python sort 使用 time sort(归并+插入)
        只需要归并操作

        执行用时：48 ms,击败 99.84%
        内存消耗：17.7 MB,击败 44.40%
    """

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tail = head = ListNode(0)
        res = []
        for node in lists:
            while node:
                res.append(node)
                node = node.next
        res.sort(key=lambda x: x.val)
        for i in res:
            tail.next = i
            tail = i
        return head.next


class Solution1:
    """
        O(n*log(k)) n 为链表节点总个数, k 为链表长度
        空间复杂度: O(log(k))

        递归版归并排序
        1. 设立哑巴节点,简化代码
            head = ListNode(0)
        2. 递归结束条件:
            if left >= len(lists):
                return None
            if left == right:
                return lists[left]
        3. 返回值:
            返回需要合并节点的头
    """

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)

        def merge(left: int, right: int) -> Optional[ListNode]:
            if left >= len(lists):
                return None
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            p1 = merge(left, mid)
            p2 = merge(mid + 1, right)
            tail = head
            while p1 and p2:
                if p1.val < p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next
                tail = tail.next
            tail.next = p1 if p1 else p2
            return head.next

        return merge(0, len(lists) - 1)
