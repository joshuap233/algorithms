# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/submissions/
# 25. K 个一组翻转链表


from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    """
        你可以设计一个只使用常数额外空间的算法来解决此问题吗？
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

        如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

        将问题拆分, 一步步优化:
        1. 反转 K 个节点:

            prev = None
            for _ in range(k):
                Next = head.next
                head.next = prev
                prev = head
                head = Next

        2. k<= 链表长度, 因此需要多次翻转,统计链表长度:

            for _ in range(le // k):
                pass

        3. 将翻转的子节点连接:
            记录 tail 与 tmp
            tail 为当前翻转子链表的头节点的上个节点
            tmp 为当前翻转子链表的头节点

            tail->next = prev(prev 最翻转链表最后一个节点,也就是新头节点)
            tail = tmp (tmp 为新链表尾部)

        4. 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序

            tail.next = head (head 为 None 则 k 为长度整数倍)
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        le = 0
        h = head
        while h:
            le += 1
            h = h.next

        if k <= 1:
            return head

        tail = dummy = ListNode(0, head)
        for _ in range(le // k):
            prev = None
            tmp = head

            for _ in range(k):
                Next = head.next
                head.next = prev
                prev = head
                head = Next
            tail.next = prev
            tail = tmp
        tail.next = head
        return dummy.next


hdr = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
s.reverseKGroup(hdr, 2)
