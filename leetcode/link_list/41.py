#   删除链表中的节点


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
    def deleteNode(self, node):
        if node.next is not None:
            node.val = node.next.val
            node.next = node.next.next


head = generate_link_list([4, 5, 1, 9])
s = Solution()
s.deleteNode(head.next)
