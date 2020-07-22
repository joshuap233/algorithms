#  颠倒二进制位


# 48ms
class Solution:
    def reverseBits(self, n: int) -> int:
        # 这里会丢失前导0
        n = str(bin(n))[2:]
        n = list(reversed(n))
        n.extend(['0'] * (32 - len(n)))
        return int(''.join(n), 2)


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
