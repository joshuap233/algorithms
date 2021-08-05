# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
# 剑指 Offer 58 - I. 翻转单词顺序

class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i for i in s.split(" ") if i]
        s.reverse()
        return ' '.join(s)


# 上面的代码可以修改
class Solution1:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

