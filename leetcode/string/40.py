#  最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = 0
        for index, char in enumerate(strs[0]):
            for string in strs[1:]:
                if not self.has_next(string, length) or string[length] != char[length]:
                    return char[0:length]

    @staticmethod
    def has_next(array, index):
        return True if index + 1 < len(array) else False


class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        target = strs[0]
        length = len(target)
        for string in strs[1:]:
            while target != string[0:length]:
                if length == 1:
                    return ""
                target = target[:length - 1]
                length -= 1
        return target


s = Solution2()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
