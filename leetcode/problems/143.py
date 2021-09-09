# https://leetcode-cn.com/problems/reorder-list/
# 143. 重排链表

from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    """
        解法1, 把节点存到 list 中即可
    """

    def reorderList(self, head: ListNode) -> None:
        h = head

        nums = []
        while head:
            nums.append(head)
            head = head.next
        le = len(nums)

        for i in range(le // 2):
            h.next = nums[i]
            h = h.next
            h.next = nums[-i - 1]
            h = h.next

        if le % 2 != 0:
            h.next = nums[le // 2]
            h = h.next
        h.next = None


class Solution:
    """
        逆序后半部分
        好恶心, 比困难题还恶心
    """

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return head

        # 找到中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 逆序
        mid = slow

        prev = None
        h = mid.next
        while h:
            n = h.next
            h.next = prev
            prev = h
            h = n
        mid.next = None

        # 插入
        h1, h2 = head, prev
        while h1 and h2:
            n1, n2 = h1.next, h2.next

            h1.next = h2
            h1 = n1

            h2.next = n1
            h2 = n2


hdr = generate_link_list([1, 2, 3, 4])
s = Solution()
s.reorderList(hdr)
