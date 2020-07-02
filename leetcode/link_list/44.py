# 合并两个有序链表


from link_list import generate_link_list, ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        link_list = self.link_list_to_list(l1)
        link_list.extend(self.link_list_to_list(l2))
        link_list = sorted(link_list, key=lambda x: x.val)
        if not link_list:
            return None
        head = link_list[0]
        for index, node in enumerate(link_list[:-1]):
            head.next = link_list[index + 1]
            head = head.next
        return link_list[0]

    @staticmethod
    def link_list_to_list(node: ListNode) -> list:
        link_list = []
        while node is not None:
            link_list.append(node)
            node = node.next
        return link_list
