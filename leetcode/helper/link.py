class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def generate_link_list(array):
    if not array:
        return None
    node = ListNode(array[0])
    now = node
    for item in array[1:]:
        now.next = ListNode(item)
        now = now.next
    return node


def iter_link_list(node: ListNode):
    while node:
        print(node.val)
        node = node.next
