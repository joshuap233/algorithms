# https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
# 剑指 Offer 53 - I. 在排序数组中查找数字 I

from typing import List


# 二分！！！ 好麻烦的边界
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                cnt = 1
                left = mid - 1
                right = mid + 1
                while right < len(nums) and nums[right] == target:
                    cnt += 1
                    right += 1

                while left >= 0 and nums[left] == target:
                    cnt += 1
                    left -= 1
                return cnt
        return 0


# 上面的代码优化，利用二分查找边界
class Solution1:
    def search(self, nums: List[int], target: int) -> int:

        def bs(low: bool):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    pass


s = Solution()
print(s.search([1, 3], 2))
