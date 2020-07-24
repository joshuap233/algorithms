# https://leetcode-cn.com/problems/palindrome-number/
# 回文数
# 你能不将整数转为字符串来解决这个问题吗？

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        length = 0
        while temp >= 1:
            temp = temp / 10
            length += 1
        while x != 0 and length != 1:
            length -= 1
            theFirst = int(x / (10 ** length))
            theLast = int(x % 10)
            if theFirst != theLast:
                return False
            x = int((x - theLast - theFirst * 10 ** length) / 10)
            length -= 1
        return True


s = Solution()
print(s.isPalindrome(1001))
