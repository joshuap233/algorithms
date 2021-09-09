# https://leetcode-cn.com/problems/4sum/
# 18. 四数之和
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        a = 0
        le = len(nums)

        while a <= le - 4:
            b = a + 1
            while b <= le - 3:
                need = target - nums[b] - nums[a]
                c, d = b + 1, le - 1
                while c < d:
                    v = nums[c] + nums[d]
                    if v < need:
                        c += 1
                    elif v > need:
                        d -= 1
                    else:
                        ret.append([nums[a], nums[b], nums[c], nums[d]])
                        tc, td = nums[c], [d]

                        while d > c and nums[c] == tc:
                            c += 1
                        while c < d and nums[d] == td:
                            d -= 1
                p = nums[b]
                while b <= le - 3 and nums[b] == p:
                    b += 1

            p = nums[a]
            while a <= le - 4 and nums[a] == p:
                a += 1
        return ret


s = Solution()
s.fourSum([2, 2, 2, 2, 2], 8)
