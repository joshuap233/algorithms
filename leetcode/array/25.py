class Solution:
    def singleNumber(self, nums) -> int:
        count = {}
        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1
        for item, key in count.items():
            if key == 1:
                return item


class Solution2:
    def singleNumber(self, nums) -> int:
        res = 0
        for item in nums:
            res = item ^ res
        return res
