# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
# 83. 删除排序链表中的重复元素

from leetcode.helper.link import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = dummy = ListNode(0)
        while head:
            if not head.next or head.next.val != head.val:
                tail.next = head
                tail = tail.next
            head = head.next
        return dummy.next
