# 缺失数字
from typing import List


# 68 ms 15.6 MB
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = max(nums)
        seq = set(range(n))
        res = list(seq - set(nums))
        # res 为空则说明为如下序列 0,1,2,3,4,...
        return res[0] if len(res) != 0 else n + 1


# 60ms 14.7 MB
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = max(nums)
        res = 0
        for item in nums:
            res ^= item
        for item in range(n + 1):
            res ^= item
        if res == 0 and res in nums:
            # r说明为如下序列 0,1,2,3,4,...
            return n + 1
        return res


s = Solution2()
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
