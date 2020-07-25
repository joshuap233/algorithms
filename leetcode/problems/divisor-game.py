# 　除数博弈
# https://leetcode-cn.com/problems/divisor-game/

memo = {1: False}
max_ = 1


# 	88 ms, 之前把memo放init里,256ms,
# 	所以这leetcode是每次重新创建一个solution对象???
class Solution:
    def divisorGame(self, n: int) -> bool:
        global max_
        if n <= max_:
            return memo[n]
        for i in range(max_ + 1, n + 1):
            # alice 取1后,n-1,
            # 此时转换为N=n-1 ,bob先手的问题
            # 且n-1 必定在memo中
            if not memo[i - 1]:
                memo[i] = True

            for divisor in range(2, i):
                x = i / divisor
                if x == int(x):
                    if not memo[i - int(x)]:
                        memo[i] = True
                        break
            if i not in memo:
                memo[i] = False
        max_ = n
        return memo[n]
