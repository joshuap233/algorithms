# 环形链表


class Solution:
    def hasCycle(self, head) -> bool:
        link_list = []

        while head is not None:
            if head in link_list:
                return True
            link_list.append(head)
            head = head.next
        return False


# O(1)（即，常量）内存解决此问题
class Solution2:
    def hasCycle(self, head) -> bool:
        # 双指针,一个指针一次迭代一步,另一个迭代两步,相遇则环存在
        head1 = head
        head2 = head
        while head is not None:
            if head1 == head2:
                return True
            head1 = head1.next
            if head2.next is None or head2.next.next is None:
                return True
            head2 = head2.next.next
        return False
