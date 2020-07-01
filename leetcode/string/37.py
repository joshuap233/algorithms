# 字符串转换整数 (atoi)


# 切割list后检查list是否为空
class Solution:
    def myAtoi(self, s: str) -> int:
        firstIndex = self.find_first_not_null_str(s)
        if firstIndex == -1:
            return 0
        s = s[firstIndex:]

        if self.is_empty(s):
            return 0

        if self.is_number(s[0]):
            number = ''
            for item in s:
                if not self.is_number(item):
                    break
                number += item
            number = int(number)
            res = self.is_overflow(number)
            return res if res else number
        else:
            signal = -1 if s[0] == '-' else 1
            s = s[1:]
            if self.is_empty(s):
                return 0
            if not self.is_number(s[0]):
                return 0
            number = ''
            for index, item in enumerate(s):
                if not self.is_number(item):
                    break
                number += item
            number = int(number) * signal
            res = self.is_overflow(number)
            return res if res else number

    def first_character_is_effect(self, c):
        return True if (self.is_number(c) or c in ['+', '-']) else False

    @staticmethod
    def is_number(c):
        return True if '0' <= str(c) <= '9' else False

    @staticmethod
    def is_overflow(c: int):
        min_ = -2 ** 31
        max_ = 2 ** 31 - 1
        if c < min_:
            return min_
        if c > max_:
            return max_
        return False

    @staticmethod
    def is_empty(c):
        return True if c == '' or [] else False

    def find_first_not_null_str(self, str_) -> int:
        firstIndex = 0
        for index, item in enumerate(str_):
            if item != ' ':
                if not self.first_character_is_effect(item):
                    return -1
                firstIndex = index
                break
            # 全为空串或没有有效数字,字符
            if index == len(str_) - 1:
                return -1
        return firstIndex


s = Solution()
print(s.myAtoi("+"))
