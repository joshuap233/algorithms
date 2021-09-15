# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# 82. 删除排序链表中的重复元素 II

from leetcode.helper.link import ListNode
from collections import Counter


class Solution:
    """升序排列的链表, 使用计数器计数"""

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        counter = Counter()
        tail = dummy = ListNode(0, None)
        hdr = head
        while hdr:
            counter[hdr.val] += 1
            hdr = hdr.next

        while head:
            if counter[head.val] == 1:
                tail.next = head
                tail = head
            head = head.next
        tail.next = None
        return dummy.next


class Solution1:
    """升序排列的链表"""

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = tail = dummy = ListNode(301)
        while head:
            while head.next and head.next.val == head.val:
                prev = head
                head = head.next
            if prev.val != head.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next
