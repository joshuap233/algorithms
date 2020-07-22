#   罗马数字转整数

# 56ms
class Solution:
    nums_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    spe = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        jump = False
        for index, item in enumerate(s):
            if jump:
                jump = False
                continue
            spe = self.special(index, item, s)
            if spe:
                jump = True
                res += spe
            else:
                res += self.nums_map[item]
        return res

    def special(self, index, item, string):
        if index + 1 >= len(string):
            return False
        next_ = string[index + 1]
        item = item + next_
        if item in self.spe:
            return self.spe[item]
        return False


s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
