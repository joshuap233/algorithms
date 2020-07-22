#  打乱数组


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        import random
        temp = self.nums.copy()
        res = []
        for i in range(len(self.nums)):
            index = random.randint(0, len(temp) - 1)
            res.append(temp[index])
            del temp[index]
        return res


obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()
