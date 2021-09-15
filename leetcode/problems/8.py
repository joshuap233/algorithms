import re


class Solution:
    MAXI = 2 ** 31 - 1
    MINI = -2 ** 31

    def myAtoi(self, s: str) -> int:
        p = r'^[ ]*([+|-]?[0-9]+)'
        r = re.match(p, s)
        if not r:
            return 0
        r = int(r.group(0))
        if r > self.MAXI:
            return self.MAXI
        if r < self.MINI:
            return self.MINI
        return r
