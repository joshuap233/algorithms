# https://leetcode-cn.com/problems/add-two-numbers-ii/
# 445. 两数相加 II

from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = b = 0
        while l1:
            a = a * 10 + l1.val
            l1 = l1.next

        while l2:
            b = b * 10 + l2.val
            l2 = l2.next
        a = str(a + b)

        tail = head = ListNode(int(a[0]))
        for i in range(1, len(a)):
            tail.next = ListNode(int(a[i]))
            tail = tail.next
        return head


s = Solution()
s.addTwoNumbers(
    generate_link_list([7, 2, 4, 3]),
    generate_link_list([5, 6, 4])
)
