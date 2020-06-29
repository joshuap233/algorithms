# 两数之和


class Solution:
    def twoSum(self, nums, target):
        values = {}
        # 存放重复值的映射
        for index, item in enumerate(nums):
            if item not in values:
                values[item] = index
            else:
                if item == target - item:
                    return [values[item], index]
        for item in values:
            diff = target - item
            if diff != item and diff in values:
                return [values[item], values[diff]]

