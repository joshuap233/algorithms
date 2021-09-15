# https://leetcode-cn.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
      O(n) 的空间复杂度与时间复杂度
    """

    def isPalindrome(self, head: ListNode) -> bool:
        value = []
        while head:
            value.append(head.val)
            head = head.next

        for i in range(len(value) // 2):
            if value[i] != value[-(i + 1)]:
                return False
        return True


class Solution1:
    """
       O(n) 时间复杂度和 O(1) 空间复杂度,
      反转一半链表再判断
    """

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            fast = fast.next.next

            Next = slow.next
            slow.next = pre
            pre = slow
            slow = Next

        while pre and slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        return True


class Solution2:
    """
        0 <= Node.val <= 9
        时间超限.......
    """
    def isPalindrome(self, head: ListNode) -> bool:
        s1 = s2 = 0
        t = 1
        while head:
            s1 = s1 * 10 + head.val
            s2 += t * head.val
            t *= 10
            head = head.next
        return s1 == s2
