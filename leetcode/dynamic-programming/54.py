# 爬楼梯


# 时间超限
class Solution:
    def __init__(self):
        self.count = 0

    def climbStairs(self, n: int) -> int:
        self.calculate_stairs(n)
        return self.count

    def calculate_stairs(self, number):
        if number <= 0:
            if number == 0:
                self.count += 1
            return
        self.calculate_stairs(number - 1)
        self.calculate_stairs(number - 2)


# 改进 32 ms
class Solution2:
    memo = {}

    def climbStairs(self, n: int) -> int:
        return self.calculate_stairs(n, 0)

    def calculate_stairs(self, number, count) -> int:
        if number in self.memo:
            return self.memo[number] + count
        if number <= 0:
            if number == 0:
                count += 1
            return count
        count = self.calculate_stairs(number - 1, count)
        count = self.calculate_stairs(number - 2, count)
        self.memo[number] = count
        return count


# 动态规划
class Solution3:
    def climbStairs(self, n: int) -> int:
        """
        转移方程
        因为一次可以移动一阶或者两阶,所以移动到当前阶的方案数
        等于 移动到前一阶 与前两阶的 和
        f(x)=f(x−1)+f(x−2)
        """
        x0 = 1
        x1 = 1
        for i in range(2, n + 1):
            x0, x1 = x1, x0 + x1
        return x1


s = Solution3()
print(s.climbStairs(4))
