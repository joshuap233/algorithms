# 汉明距离
# 40ms
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        n = str(bin(n))
        count = 0
        for item in n:
            if item == '1':
                count += 1
        return count


s = Solution()
print(s.hammingDistance(1, 4))
