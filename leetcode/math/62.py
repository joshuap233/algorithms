#   3的幂

class Solution:
    memo = {}
    max = 0

    def isPowerOfThree(self, n: int) -> bool:
        count = 0

        if n in self.memo:
            return True
        if n < self.max:
            return False

        while True:
            res = 3 ** count
            if n < res:
                return False
            if n == res:
                self.memo[res] = 1
                self.max = n
                return True
            count += 1
            self.memo[res] = 1


s = Solution()
print(s.isPowerOfThree(4))
