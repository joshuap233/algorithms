# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
# 剑指 Offer 48. 最长不含重复字符的子字符串

# 遍历一遍,将 value:index 键值对存入字典,
# 当遇到 value 已经在字典中时,记录最大值
# max(maxi,i(当前索引) -left), 并更新索引
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = maxi = 0
        for i, v in enumerate(s):
            if v in d and d[v] >= left:
                maxi = max(maxi, i - left)
                left = d[v] + 1
            d[v] = i
        return max(maxi, len(s) - left)


s = Solution()
print(s.lengthOfLongestSubstring("cdd"))
