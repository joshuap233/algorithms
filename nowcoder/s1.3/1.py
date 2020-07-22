#
#
# @param x string字符串 字符串从前到后分别是从上到下排列的n张扑克牌
# @return string字符串
#


class Solution:
    def Orderofpoker(self, x: str):
        res = ''
        while x != '':
            if self.isPrime(len(x)/2):
                res += ''.join(x[0:2])
                x = x[2:]
            else:
                res += ''.join(x[-2:])
                x = x[:-2]
        return res

    @staticmethod
    def isPrime(n):
        import math
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


s = Solution()
print(s.Orderofpoker("3C8D6H3D"))
