# 两个数组的交集 II
class Solution:
    def intersect(self, nums1, nums2):
        new_list = []
        self.find_common(new_list, nums1, nums2)
        return new_list

    @staticmethod
    def find_common(new_list, nums1, nums2):
        for item in nums1:
            for index2, item2 in enumerate(nums2):
                if item == item2:
                    nums2.pop(index2)
                    new_list.append(item)
                    break


s = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2]
print(s.intersect(nums1, nums2))
