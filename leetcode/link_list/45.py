#   回文链表

from link_list import generate_link_list, ListNode


class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return True
        link_list = self.link_list_to_list(head)
        for index in range(len(link_list) // 2):
            if link_list[index].val != link_list[-(index + 1)].val:
                return False
        return True

    @staticmethod
    def link_list_to_list(node) -> list:
        link_list = []
        while node is not None:
            link_list.append(node)
            node = node.next
        return link_list


# O(n) 时间复杂度和 O(1)空间复杂度
# 找到中点,断开链表
class Solution2:
    def isPalindrome(self, head) -> bool:
        if not head:
            return True
        c_point_index = self.find_center_point(head)
        head1, head2 = self.break_link_list(head, c_point_index)
        head2 = self.reserved_link_list(head2, None)
        # head1 的链表可能比head2的多一个元素,所以head2,head1 都不为None才继续循环
        while head1 is not None and head2 is not None:
            if head1.val != head2.val:
                return False
            head2 = head2.next
            head1 = head1.next
        return True

    @staticmethod
    def find_center_point(head):
        index = -1
        now = head
        while now is not None:
            index += 1
            now = now.next
        return index // 2

    @staticmethod
    def break_link_list(head: ListNode, center_point: int) -> tuple:
        index = 0
        head1 = head
        while index != center_point:
            head = head.next
            index += 1
        head2 = head.next
        # 断开链表
        head.next = None

        return head1, head2

    # 原地反转链表(递归
    def reserved_link_list(self, cur_node, pre_node) -> ListNode:
        if cur_node is None:
            return pre_node
        next_ = cur_node.next
        cur_node.next = pre_node
        return self.reserved_link_list(next_, cur_node)


# h = generate_link_list([0, 1, 2, 3, 4])
# s = Solution()
# print(s.isPalindrome(h))

h = generate_link_list([1])
s = Solution2()
print(s.isPalindrome(h))
