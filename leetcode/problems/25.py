# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/submissions/
# 25. K 个一组翻转链表


from leetcode.helper.link import ListNode, generate_link_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cnt = 0
        h = head
        while h:
            cnt += 1
            h = h.next

        dummy = tail = ListNode(0, head)
        cur = tail.next
        prev = None
        for i in range(cnt // k):
            for j in range(k):
                Next = cur.next
                cur.next = prev
                prev = cur
                cur = Next
            tmp = tail.next
            tail.next = prev
            tail = tmp
            tail.next = cur
        return dummy.next


hdr = generate_link_list([1, 2, 3, 4, 5])
s = Solution()
s.reverseKGroup(hdr, 2)
