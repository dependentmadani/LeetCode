import numpy as np
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = []

        # # for i in range(len(nums)):
        # #     product = 1
        # #     for j in range(len(nums)):
        # #         if (j != i):
        # #             product *= nums[j]
        # #     answer.append(product)
        # answer = np.array(nums)
        
        # output = answer.prod() / answer
        # hada = []
        # for i in output:
        #     if (math.isnan(i)):
        #         hada.append(0)
        #     else:
        #         hada.append(int(i))
        length_nums = len(nums)
        answer = [1] * length_nums
        before = 1
        after = 1
        for i in range(length_nums):
            answer[i] *= before
            before = before * nums[i]
            answer[length_nums - i - 1] *= after
            after = after * nums[length_nums - i - 1]

        # output = output.astype(int)
        return answer
