# 有效的括号
class Solution:
    string = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    left = string.keys()

    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in self.left:
                stack.append(self.string[item])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop(-1)
                if top != item:
                    return False
        if len(stack) != 0:
            return False
        return True


s = Solution()
print(s.isValid("["))
