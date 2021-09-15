from leetcode.helper.link import ListNode


class Solution:
    """
        添加加到数组里,然后连接
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        nums = []
        h = head
        while h:
            nums.append(h)
            h = h.next

        tail = dummy = ListNode(0)
        for i in range(0, len(nums), 2):
            tail.next = nums[i]
            tail = tail.next
        for i in range(1, len(nums), 2):
            tail.next = nums[i]
            tail = tail.next
        tail.next = None
        return dummy.next


class Solution1:
    """

        请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，
        时间复杂度应为 O(nodes)，nodes 为节点总数。

        创建奇链表与偶链表,然后连接
    """

    def oddEvenList(self, head: ListNode) -> ListNode:
        tail1 = dummy1 = ListNode(0)  # 奇
        tail2 = dummy2 = ListNode(0)
        i = 0
        while head:
            if i % 2 == 0:
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
            i += 1
        tail1.next = dummy2.next
        tail2.next = None
        return dummy1.next
