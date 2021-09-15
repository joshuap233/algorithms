from leetcode.helper.tree import TreeNode
from typing import List, Optional
from collections import deque
from leetcode.helper.tree import generate_tree


class Solution:
    """
        注意,距离为 k 的点不经包括父节点,子节点...
        还有兄弟节点,兄弟的儿子....都需要计算
        树上的每个结点都具有唯一的值 0 <= node.val <= 500

        解法: 哈希表记录父节点,建图深搜
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def recur(node: TreeNode):
            if not node or node == target:
                return

            if node.left:
                parent[node.left.val] = node
                recur(node.left)
            if node.right:
                parent[node.right.val] = node
                recur(node.right)

        if not root:
            return []

        parent = {}
        q = deque([target])
        recur(root)
        while k:
            for i in range(len(q)):
                e = q.popleft()
                if e.left and e.left.val >= 0:
                    q.append(e.left)
                if e.right and e.right.val >= 0:
                    q.append(e.right)
                if e.val in parent and parent[e.val].val >= 0:
                    q.append(parent[e.val])
                e.val = -1
            k -= 1
        return [i.val for i in q]


t = generate_tree([0, 1, 3, None, 2])
s = Solution()
s.distanceK(t, t.left, 2)
