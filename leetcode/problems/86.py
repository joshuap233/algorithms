from leetcode.helper.link import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        tail1 = dummy1 = ListNode(0)  # < x
        tail2 = dummy2 = ListNode(0)  # >= x
        while head:
            if head.val < x:
                tail1.next = head
                tail1 = head
            else:
                tail2.next = head
                tail2 = head
            head = head.next

        tail1.next = dummy2.next
        tail2.next = None
        return dummy1.next
