# Definition for singly-linked list.
from leetcode.helper.link import generate_link_list, iter_link_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 两数相加 80 ms
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        res = str(int(num1) + int(num2))
        res = ''.join(list(reversed(res)))
        node = ListNode(int(res[0]))
        head = node
        for item in res[1:]:
            node.next = ListNode(int(item))
            node = node.next
        return head


s1 = generate_link_list([2, 4, 3])
s2 = generate_link_list([5, 6, 4])
s = Solution()
node = s.addTwoNumbers(s1, s2)
iter_link_list(node)
