class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0,0]

        numbers = sorted(nums)
        break_point = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                # if (numbers[j] > target):
                #     break
                # if (numbers[i] + numbers[j] == target):
                #     first_index = nums.index(numbers[i])
                #     nums.pop(first_index)
                #     result = [first_index, nums.index(numbers[j]) + 1]
                #     break_point = 1
                #     break
                if (nums[i] + nums[j] == target):
                    result = [i, j]
                    break_point = 1
                    break
            if break_point == 1:
                break
        return result
