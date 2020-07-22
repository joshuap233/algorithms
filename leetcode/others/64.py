# 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        count = 0
        for item in n:
            if item == '1':
                count += 1
        return count


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
