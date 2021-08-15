# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
# 剑指 Offer 38. 字符串的排列
from typing import List


# 递归
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()

        def recur(head: str, string: str):
            if not string:
                res.add(head)
            for i, v in enumerate(string):
                recur(head + v, string[:i] + string[i + 1:])

        recur('', s)

        return list(res)


class Solution1:
    def permutation(self, s: str) -> List[str]:
        res = set()
        s = list(s)

        def backtrace(left: int):
            if left == len(s):
                res.add(''.join(s))

            for i in range(left, len(s)):
                s[left], s[i] = s[i], s[left]
                backtrace(left + 1)
                s[left], s[i] = s[i], s[left]

        backtrace(0)

        return list(res)


# 即获取下一个字典序排列
# 类似: https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
class Solution2:
    """
        重复寻找下一个字典序, 很明显需要找到一个尽量靠右的数 s[j](变化的尽量是低位)
        与 s[j] 恰好比当前的数大的数交换,交换后序列为  s[x] .... s[j] .... (交换前为: s[j] ... s[x]....)
        且 s[x] 右边的数必须为升序排列, 否则 s[x] 右边还有可以交换的数

        最后的字典序为: 序列为降序排列(无法找到下一个字典序)
    """

    def permutation(self, s: str) -> List[str]:
        res = []
        tmp = sorted(s)
        res.append(''.join(tmp))

        while True:
            i = len(tmp) - 2

            while i >= 0 and tmp[i] >= tmp[i + 1]:
                i -= 1

            if i >= 0:
                j = len(tmp) - 1
                while j > i and tmp[j] <= tmp[i]:
                    j -= 1
                tmp[j], tmp[i] = tmp[i], tmp[j]

                left, right = i + 1, len(tmp) - 1
                # 逆序,保证右边的数为升序排列
                while left < right:
                    tmp[left], tmp[right] = tmp[right], tmp[left]
                    left += 1
                    right -= 1
                res.append(''.join(tmp))
            else:
                return res


s = Solution1()
print(s.permutation("abc"))
