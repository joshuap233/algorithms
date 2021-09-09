# https://leetcode-cn.com/problems/remove-k-digits/solution/
# 402. 移掉 K 位数字


from collections import deque


class Solution:
    """
        暴力解法: 遍历一遍,决定是否要移除相邻元素
        当前元素为 a,左边元素为 l,右边元素为 r
        a > r,移除 r
        a < l,移除 l
        可以用栈模拟
    """

    # 构建递增栈
    def removeKdigits(self, num: str, k: int) -> str:
        queue = deque()

        for i in num:
            while k and queue and queue[-1] > i:
                queue.pop()
                k -= 1
            queue.append(i)

        while k:
            queue.pop()
            k -= 1

        return (''.join(queue)).lstrip('0') or '0'


s = Solution()
print(s.removeKdigits("2222", 1))
