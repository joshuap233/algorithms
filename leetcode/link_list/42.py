# 删除链表的倒数第N个节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_link_list(array):
    node = ListNode(array[0])
    now = node
    for item in array[1:]:
        now.next = ListNode(item)
        now = now.next
    return node


class Solution:
    def removeNthFromEnd(self, head, n: int):
        link_list = []
        now = head
        count = 0
        while now is not None:
            link_list.append(now)
            count += 1
            now = now.next
        if n == count:
            return None if count == 1 else link_list[1]
        pre_delete = link_list[-(n + 1)]
        pre_delete.next = pre_delete.next.next
        return head


head = generate_link_list([1])
s = Solution()
res = s.removeNthFromEnd(head, 1)
print(res)
