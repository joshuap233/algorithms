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
       没说不能修改链表?? 算法结束改回来就行....
       感觉会限制修改链表...

        mmp 官方题解就是修改链表再改回来.....说你*呢....
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
