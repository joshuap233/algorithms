from leetcode.helper.tree import TreeNode
from leetcode.helper.link import ListNode
from typing import Optional


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def recur(ll: int, rr: int) -> Optional[TreeNode]:
            if ll > rr:
                return TreeNode(nums[ll])

            mid = (ll + rr) // 2
            node = TreeNode(nums[mid])
            node.left = recur(ll, mid - 1)
            node.right = recur(mid + 1, rr)
            return node

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return recur(0, len(nums) - 1)


class Solution1:
    """
        空间优化()
    """

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        prev.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node
