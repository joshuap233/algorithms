from typing import List


class Solution:
    """
        时间复杂度 O(k*n), 时间超限.....
    """

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        for _ in range(k):
            tmp = nums[-1]
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = nums[i - 1]
            nums[0] = tmp


class Solution1:
    """
        时间复杂度 O(n)
        空间复杂度 O(1)
        三次逆序
        1. 整个数组
        2. 逆序前 k 的数
        3  逆序后 len-k 个澍
    """

    def rotate(self, nums: List[int], k: int) -> None:
        le = len(nums)
        k = k % le
        if k == 0:
            return
        nums[:] = nums[::-1]
        nums[:k] = nums[k - 1::-1]
        nums[k:] = nums[le - 1:k - 1:-1]


class Solution1:
    """
        可惜空间复杂度不是 O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        le = len(nums)
        k = k % le
        nums[:] = nums[le - k:] + nums[:le - k]


a = [1, 2, 3, 4, 5, 6, 7]
s = Solution1()
s.rotate(a, 3)
print(a)
