# https://leetcode-cn.com/problems/string-compression/
# 443. 压缩字符串
from typing import List


class Solution:
    """
        请在 修改完输入数组后 ，返回该数组的新长度。

        如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为
        多个字符。
    """

    def compress(self, chars: List[str]) -> int:
        p = i = 0  # p 指向可填入字母的索引
        le = len(chars)
        while i < le:
            cnt = 1
            while i + 1 < le and chars[i] == chars[i + 1]:
                cnt += 1
                i += 1
            chars[p] = chars[i]
            p += 1
            if cnt > 1:
                for j in str(cnt):
                    chars[p] = j
                    p += 1
            i += 1
        return p


s = Solution()
s.compress(["a", "a", "b", "b", "c", "c", "c"])
