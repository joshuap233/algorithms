from leetcode.helper.tree import TreeNode, generate_tree
from collections import deque


class Solution:
    """
        从左到右遍历, 遇到空节点设置 flag,
        设置 flag 后在遇到 非空节点返回 False
    """
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        end = False
        while queue:
            for i in range(len(queue)):
                e = queue.popleft()
                if e:
                    if end:
                        return False
                    queue.append(e.left)
                    queue.append(e.right)
                else:
                    end = True
        return True


node = generate_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 15])
s = Solution()
s.isCompleteTree(node)
