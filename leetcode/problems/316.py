# 与 1081 题相同
# https://leetcode-cn.com/problems/remove-duplicate-letters/
# 316. 去除重复字母
from collections import Counter, deque


class Solution:
    """
        这题不能用哈希去重然后排序,只能在删除过程中保证字典序最小
        与 T402 类似,

        但是只有重复元素可以去除,并且最后该元素需要剩余一个
        因此构建单调栈的过程中, 前面的元素不一定为为递增栈,
        比如
         acdb, 由于 b 元素无法删除, 因此不再是单调栈,
         当 c 元素入栈时, 由于栈内 c 已经存在, 因此当前元素不入栈,
         如果删除栈内 c, 必然导致字典序增大
    """

    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        q = deque()
        for i in s:
            if i not in q:
                while q and q[-1] >= i and c[q[-1]]:
                    q.pop()
                q.append(i)
            c[i] -= 1
        return ''.join(q)


s = Solution()
ret = s.removeDuplicateLetters("cdadabcc")
print(ret)
