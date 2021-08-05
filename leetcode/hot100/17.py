# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
# 17. 电话号码的字母组合
from typing import List


class Solution:
    """
        回溯法....
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        string = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def traceback(num: int, array: List[str]):
            if num == len(digits):
                res.append(''.join(array))
                return
            for i in string[int(digits[num]) - 2]:
                array.append(i)
                traceback(num + 1, array)
                array.pop(-1)

        traceback(0, [])
        return res


s = Solution()
s.letterCombinations("23")
