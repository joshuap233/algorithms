# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
# 83. 删除排序链表中的重复元素

from leetcode.helper.link import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        tail = head
        tmp = head
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = head
            head = head.next
        tail.next = None
        return tmp
