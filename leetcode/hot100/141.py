# https://leetcode-cn.com/problems/linked-list-cycle/
# 141. 环形链表
# 解法: 1.快慢双指针 2.哈希表 3.直接为节点赋值

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        p1, p2 = head, head.next
        while p1 != p2:
            if not p2 or not p2.next:
                return False

            p1 = p1.next
            p2 = p2.next.next
        return True
