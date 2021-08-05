# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# 剑指 Offer 46. 把数字翻译成字符串


class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        cnt = 0

        def recur(p: int):
            nonlocal cnt
            if p >= len(num) - 1:
                cnt += 1
                return
            recur(p + 1)
            if p < len(num) - 1 and '10' <= num[p] + num[p + 1] <= '25':
                recur(p + 2)

        recur(0)
        return cnt


s = Solution()
res = s.translateNum(12258)
print(res)
