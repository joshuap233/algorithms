# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        tmp = [i for i in nums if i % 2 == 0]
        tmp1 = [i for i in nums if i % 2 != 0]
        tmp1.extend(tmp)
        return tmp1


# 首尾双指针
class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if nums[p1] % 2 == 0:
                while p1 < p2:
                    if nums[p2] % 2 != 1:
                        p2 -= 1
                    else:
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        break
            p1 += 1
        return nums


class Solution3:
    """更简洁..."""
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1:
                left += 1
                continue
            if nums[right] % 2 == 0:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        return nums


s = Solution2()
res = s.exchange([1, 2, 3, 4])
print(res)
