import numpy as np

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_set = 1
        tmp_longest_set = 1
        nums.sort()
        data = np.array(nums)
        result = np.unique(data)
        if (not nums):
            return 0
        number = nums[0]
        
        for i in range(len(result)):
            if (i == 0):
                number += 1
                continue
            if (result[i] == number):
                print(result[i])
                number += 1
                tmp_longest_set += 1
                if (tmp_longest_set > longest_set):
                    longest_set = tmp_longest_set
            else:
                number = result[i]
                tmp_longest_set = 1
                number += 1
        return longest_set
