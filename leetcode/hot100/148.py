# https://leetcode-cn.com/problems/sort-list/
# 148. 排序链表
from math import floor
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
     O(n log n) 时间复杂度
     O(n) 空间复杂度
    """

    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        s = []
        while head:
            s.append(head)
            head = head.next
        s.sort(key=lambda x: x.val)

        head = s[0]
        for i in s[1:]:
            head.next = i
            head = i
        s[-1].next = None
        return s[0]


class Solution1:
    """
    你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，
    对链表进行排序吗？

    用归并排序迭代法....归并的递归也是算空间复杂度的....

    我服了，这么长的代码面试写你妈呢

    1.
    先 统计链表长度

    2.
    归并的时候需要写额外的代码判断头结点:
        if head1.val < head2.val:
        head3 = tail3 = head1
        head1 = head1.next
    else:
        head3 = tail3 = head2
        head2 = head2.next
    不如 直接添加一个哑巴节点 dummyNode 作为头结点

    3.
    找到一组节点之后,最后一个节点的 next 置 None
    """

    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1: ListNode, h2: ListNode) -> ListNode:
            dummyHead, dummyTail = ListNode(0)
            while h1 and h2:
                if h1.val < h2.val:
                    dummyTail.next = h1
                    h1 = h1.next
                else:
                    dummyTail.next = h2
                    h2 = h2.next
            dummyTail.next = h1 if h1 else h2
            return dummyHead.next

        def move_to(h1: Optional[ListNode], k: int) -> ListNode:
            while h1 and k > 0:
                h1 = h1.next
                k -= 1
            return h1

        # 统计节点个数
        cnt = 0
        while head:
            cnt += 1
            head = head.next

        step = 1
        cnt = floor(cnt / 2)

        dummyHead = ListNode(0, head)
        while step <= cnt:
            cur = dummyHead.next
            while cur:
                # 找到 最后一个节点
                head1 = move_to(cur, step)
                head2 = move_to(head1.next, step)

                # 置空最后一个节点
                tmp = head2.next

                head2.next = None
                head2 = head1.next

                head1.next = None
                head1 = cur

                # 归并
                newHead = merge(head1, head2)

                # 连接归并后的节点
                if cur == dummyHead.next:
                    dummyHead.next = newHead
                else:
                    cur.next = newHead
                cur = tmp

            step += step
        return dummyHead.next

