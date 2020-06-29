# 删除排序数组中的重复项


class Solution:

    def removeDuplicates(self, nums) -> int:
        max_length = len(nums)
        length = 0
        offset = 0
        for index, item in enumerate(nums):
            if max_length > (index + 1) and item == nums[index + 1]:
                continue
            nums[length] = item
            length += 1
        return length


nums = [0, 0, 0, 1, 1, 1, 4, 5]
s = Solution()
length = s.removeDuplicates(nums)
for i in range(length):
    print(nums[i])
