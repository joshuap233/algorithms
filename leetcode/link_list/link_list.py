class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_link_list(array):
    if not array:
        return None
    node = ListNode(array[0])
    now = node
    for item in array[1:]:
        now.next = ListNode(item)
        now = now.next
    return node
