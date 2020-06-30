# 字符串中的第一个唯一字符

class Solution:
    def firstUniqChar(self, s: str) -> int:
        array = list(s)
        dup = set()
        for index, item in enumerate(array):
            if item in dup:
                continue
            is_first_uniq_char = True
            for index1, item1 in enumerate(array[index + 1:]):
                if item1 == item:
                    dup.add(item)
                    is_first_uniq_char = False
                    break
            if is_first_uniq_char:
                return index
        return -1


s = Solution()
res = s.firstUniqChar("aadadaad")
print(res)
