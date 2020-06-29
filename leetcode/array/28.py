# 移动零


class Solution:
    def moveZeroes(self, nums: list) -> None:
        index = 0
        count = len(nums)
        while count > 0:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            count -= 1


class Solution2:
    def moveZeroes(self, nums: list) -> None:
        countZero = 0
        trueIndex = 0
        for index, item in enumerate(nums):
            if item != 0:
                nums[trueIndex] = item
                trueIndex += 1
            else:
                countZero += 1
        maxIndex = len(nums) - 1
        while countZero > 0:
            nums[maxIndex - countZero + 1] = 0
            countZero -= 1


s = Solution2()
s.moveZeroes([0, 1, 0, 3, 12])
