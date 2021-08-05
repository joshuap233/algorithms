# https://leetcode-cn.com/problems/3sum/
# 15. 三数之和
from typing import List


class Solution:
    """
     O(n*n)时间复杂度 ......

     这题难点在于去重, 直接暴力解,时间复杂度是 O(n*n*n),
     去重很慢,set 并不能对 三元组去重..... 除非是排序的三元组

     比如 s = {[1,2,3]}
     s1 = [1,2,3]
     s1 in s -> True
     [3,2,1] in s -> False


     对于每一重循环而言，相邻两次枚举的元素不能相同，否则也会造成重复,

     优化
     如果有 a + b + c = 0
     第二重循环向后枚举一个元素时, b -> b', 因为以及排序,所以 b'> b
     所以 c' < c, 即 c' 在 c 的左侧, 因此可以
     重小到大枚举 b, 从大到小枚举 c , 时间复杂度为 O(n)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            # 去重
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            c = len(nums) - 1
            for b in range(a + 1, len(nums)):
                # 去重
                if b != a + 1 and nums[b] == nums[b - 1]:
                    continue

                target = -(nums[a] + nums[b])
                # 第三重循环不需要去重, 这重循环本质上就是第二重循环
                while b < c and nums[c] > target:
                    c -= 1

                # 指针重合, 接下来的数是重复的数,直接跳出循环
                if b == c:
                    break

                if nums[c] == target:
                    res.append([nums[a], nums[b], nums[c]])

        return res


class Solution1:
    """
        上面的代码改了下,
        第一重循环去除之后,题目就变成了排序数组的两数之和, 双指针题
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            # 去重
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            ll, r = a + 1, len(nums) - 1
            while ll < r:
                # 去重
                if ll != a + 1 and nums[ll] == nums[ll - 1]:
                    ll += 1
                    continue

                target = -(nums[ll] + nums[a])
                while ll < r and nums[r] > target:
                    r -= 1
                if ll < r and nums[r] == target:
                    res.append([nums[a], nums[ll], nums[r]])
                ll += 1
        return res


s = Solution1()
print(s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
