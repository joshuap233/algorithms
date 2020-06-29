# 旋转数组


class Solution:
    def rotate(self, nums, k) -> None:
        length = len(nums)
        k = k % length
        self.reserve(nums, 0, length - k - 1)
        self.reserve(nums, length - k, length - 1)
        self.reserve(nums, 0, length - 1)

    @staticmethod
    def reserve(array, start, end):
        index = start
        length = len(array[start: end + 1]) // 2
        count = 0
        while count < length:
            array[index], array[end - (index - start)] = array[end - (index - start)], array[index]
            index += 1
            count += 1


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
print(nums)
