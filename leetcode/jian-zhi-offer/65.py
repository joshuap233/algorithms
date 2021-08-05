# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
# 剑指 Offer 65. 不用加减乘除做加法


# 无进位和 与 异或运算 规律相同，进位 和 与运算 规律相同（并需左移一位）。
class Solution:
    """
    JAVA:写法
    while(b != 0) { // 当进位为 0 时跳出
        int c = (a & b) << 1;  // c = 进位
        a ^= b; // a = 非进位和
        b = c; // b = 进位
    }
    return a;
    """
    def add(self, a: int, b: int) -> int:
        pass


s = Solution()
s.add(1, 3)
