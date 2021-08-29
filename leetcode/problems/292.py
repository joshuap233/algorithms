# https://leetcode-cn.com/problems/nim-game/
# 292. Nim 游戏


class Solution:
    """先用暴力解题,然后找规律"""

    def canWinNim(self, n: int) -> bool:
        return n % 4 == 0
