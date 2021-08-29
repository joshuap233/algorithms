# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
# 237. 删除链表中的节点
from leetcode.helper.link import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
