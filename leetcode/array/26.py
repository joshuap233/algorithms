class Solution:
    def intersect(self, nums1, nums2):
        new_list = []
        self.find_common(new_list, nums1, nums2)
        self.find_common(new_list, nums2, nums1)
        return new_list

    @staticmethod
    def find_common(new_list, nums1, nums2):
        for item in nums1:
            if item in nums2:
                new_list.append(item)
                nums1.remove(item)
                nums2.remove(item)


s = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(s.intersect(nums1, nums2))
