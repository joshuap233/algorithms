# Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int):
        return list(map(lambda num: self.get_str(num), range(1, n + 1)))

    @staticmethod
    def get_str(n):
        if n % 15 == 0:
            return 'FizzBuzz'
        if n % 3 == 0:
            return 'Fizz'
        if n % 5 == 0:
            return 'Buzz'
        return str(n)


s = Solution()
print(s.fizzBuzz(15))
