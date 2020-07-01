class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())

        index = 0
        while index < len(s):
            if not self.is_alphabet_or_number(s[index]):
                s.pop(index)
            else:
                index += 1

        for index in range(len(s) // 2):
            if s[index] != s[-(index + 1)]:
                return False
        return True

    @staticmethod
    def is_alphabet_or_number(value):
        return True if ('a' <= value <= 'z') or ('0' <= value <= '9') else False


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
