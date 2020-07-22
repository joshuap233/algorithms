#  计数质数
class Solution:
    memo = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 1}

    def countPrimes(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        start = self.get_start_from_memo(n)
        count = self.memo[start]
        for i in range(start, n):
            if self.is_prime(i):
                count += 1
        self.memo[n] = count
        return count

    def get_start_from_memo(self, n):
        keys = list(self.memo.keys())
        for index, key in enumerate(keys):
            if index + 1 >= len(keys):
                return key
            next_key = keys[index + 1]
            if key <= n <= next_key:
                return key

    @staticmethod
    def is_prime(n):
        import math
        for i in range(2, math.floor(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


# 厄拉多塞筛法 8992ms......上个还快一点....
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        circled = []
        data = range(2, n)
        while True:
            circled_nums = self.find_circle(data, circled)
            if circled_nums ** 2 > n:
                return len(list(data))
            data = list(filter(lambda x: x == circled_nums or x % circled_nums != 0, data))
            circled.append(circled_nums)

    @staticmethod
    def find_circle(data, circled):
        for i in data:
            if i not in circled:
                return i


# 厄拉多塞筛法,
# 用一个数组记录出所有被标记数的倍数 1228ms....
class Solution3:
    def countPrimes(self, n: int) -> int:
        from array import array
        nums = array('I', [0] * n)
        count_primes = 0
        for i in range(2, n):
            if nums[i] == 0:
                count = 1
                index = i * count
                while index < n:
                    nums[index] = 1
                    count += 1
                    index = i * count
                count_primes += 1
        return count_primes


s = Solution3()
print(s.countPrimes(4))
print(s.countPrimes(11))
