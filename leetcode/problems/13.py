# https://leetcode-cn.com/problems/roman-to-integer/
# 13. 罗马数字转整数


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        ret = 0
        i = 0
        sp = {'I', 'X', 'C'}
        while i < len(s):
            if i + 1 < len(s) and s[i] in sp:
                v = s[i:i + 2]
                if s[i:i + 2] in m:
                    ret += m[v]
                    i += 2
                    continue
            ret += m[s[i]]
            i += 1
        return ret
