# https://leetcode-cn.com/problems/next-greater-element-iii/
# 556. 下一个更大元素 III


class Solution:
    """与下一个字典序的写法一样"""
    MAXI = 2 ** 31 - 1

    def nextGreaterElement(self, n: int) -> int:
        if n <= 9:
            return -1

        s = list(str(n))

        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                break
        else:
            return -1

        for j in range(len(s) - 1, i, -1):
            if s[j] > s[i]:
                break
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = s[len(s) - 1:i:-1]  # 逆序
        ret = int(''.join(s))
        return ret if ret <= self.MAXI else -1
