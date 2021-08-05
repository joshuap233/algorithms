# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. 找到所有数组中消失的数字


from typing import List


class Solution:
    """
        简单的方法就是用set记录,然后遍历 range(1,n),判断是否在
        set 中

        进阶：你能在不使用额外空间且时间复杂度为 O(n)
        的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

        O(n) 是要只遍历一遍啊,又不能用额外空间....
        那就需要修改原数组了....
        这题数据的特殊的地方在于,数字在 [1,n]区间内,

        具体来说，遍历 nums，每遇到一个数 x，就让 nums[x−1] 增加 n。
        由于 nums 中所有数均在 [1,n] 中，增加以后，这些数必然大于 n。
        最后我们遍历 nums，若 nums[i] 未大于 n，就说明没有遇到过数 i+1。
        这样我们就找到了缺失的数字。
        注意，当我们遍历到某个位置时，其中的数可能已经被增加过，因此需要对 n 取模来还原出它本来的值。

    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """这方法还不如直接用set快"""
        n = len(nums)
        for i in nums:
            nums[i % n - 1] += n
        return [i + 1 for i, num in enumerate(nums) if num <= n]


s = Solution()
s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
