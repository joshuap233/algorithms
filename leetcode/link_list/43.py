#   反转链表

from link_list import generate_link_list, ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        link_list = []
        while head is not None:
            link_list.append(head)
            head = head.next
        if not link_list:
            return None
        link_list = list(reversed(link_list))
        for index, item in enumerate(link_list):
            if item == link_list[-1]:
                item.next = None
            else:
                item.next = link_list[index + 1]
        return link_list[0]


# 递归反转链表
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return self.reserved_link_list(head, None)

    def reserved_link_list(self, cur_node, pre_node) -> ListNode:
        if cur_node is None:
            return pre_node
        next_ = cur_node.next
        cur_node.next = pre_node
        return self.reserved_link_list(next_, cur_node)


head = generate_link_list([])
s = Solution()
s.reverseList(head)
