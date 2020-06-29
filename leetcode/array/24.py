#  存在重复元素


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums = sorted(nums)
        for index, item in enumerate(nums):
            if index == 0:
                continue
            if item == nums[index - 1]:
                return True
        return False


class Solution1:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))


s = Solution()
# s1 = Solution1()
print(s.containsDuplicate([1, 2, 3, 1]))
