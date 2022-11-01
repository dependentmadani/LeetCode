class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums = nums1
        nums.extend(nums2)
        nums.sort()
        if (len(nums) % 2 != 0):
            pos = int((len(nums) + 1) / 2 - 1)
            return float(nums[pos])
        else:
            pos1 = int(len(nums) / 2 - 1)
            pos2 = int(len(nums) / 2)
            return float((nums[pos1] + nums[pos2]) / 2)
        return 0.0