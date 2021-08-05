# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
# 剑指 Offer 20. 表示数值的字符串
# 这题太恶心了....


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        e = False
        dot = False

        j = 0
        if not s[j].isdigit():
            if s[j] in '+-':
                j += 1
            elif s[j] == '.':
                j += 1
                dot = True
                if not (j < len(s) and s[j].isdigit()):
                    return False
            else:
                return False
        # 上面的代码保证从数字开始迭代

        while j < len(s):
            prev, cur = s[j - 1], s[j]
            _next = None if j + 1 >= len(s) else s[j + 1]

            if cur.isdigit():
                j += 1
                continue

            if cur == '.':
                if not e and not dot and (prev.isdigit() or (_next and _next.isdigit())):
                    j += 1
                    dot = True
                    continue
                return False

            if cur in '+-':
                if prev in 'eE' and _next and _next.isdigit():
                    j += 1
                    continue
                return False

            if cur in 'eE':
                if (prev.isdigit() or prev == '.') and not e and _next and (_next.isdigit() or _next in '+-'):
                    e = True
                    j += 1
                    continue
                return False

            return False
        return True

