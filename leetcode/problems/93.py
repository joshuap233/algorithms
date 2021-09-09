# https://leetcode-cn.com/problems/restore-ip-addresses/
# 93. 复原 IP 地址
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        cur = []
        n = len(s)

        def backtrace(left: int):
            if cur and (int(cur[-1]) > 255 or (len(cur[-1]) == 1 or cur[-1][0] != '0')):
                return
            if len(cur) == 4:
                if left == n:
                    res.append('.'.join(cur))
                return

            c = ''
            for i in range(left, min(left + 3, n)):
                c += s[i]
                cur.append(c)
                backtrace(i + 1)
                cur.pop(-1)

        backtrace(0)
        return res


class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrace(left: int):
            if cur:
                last = cur[-1]
                if len(last) > 1 and last[0] == '0':
                    return
                if len(last) == 3 and int(last) > 255:
                    return
            if len(cur) == 4:
                if left < le:
                    return
                ret.append('.'.join(cur))

            for i in range(left, min(le, left + 3)):
                cur.append(s[left:i + 1])
                backtrace(i + 1)
                cur.pop(-1)

        le = len(s)
        cur = []
        ret = []
        backtrace(0)
        return ret
