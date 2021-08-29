# https://leetcode-cn.com/problems/implement-rand10-using-rand7/
# 470. 用 Rand7() 实现 Rand10()
import random


def rand7() -> int:
    return random.randint(1, 7)


class Solution:
    def rand10(self) -> int:
        def rand2() -> int:
            a = 7
            while a == 7:
                a = rand7()
            return 0 if a <= 3 else 1

        v = 11
        while v > 10 or v == 0:
            v = 0
            for i in range(4):
                b = rand2()
                v = (v << 1) | b
        return v


class Solution1:
    # 五分之一 * 二分之一
    def rand10(self) -> int:
        a, b = 6, 7
        # 五分之一的概率
        while a > 5:
            a = rand7()

        # 二分之一的概率为 0-3, 二分之一为 3-6
        while b == 7:
            b = rand7()
        return (0 if b <= 3 else 5) + a


s = Solution1()
for i in range(1000):
    print(s.rand10())
