class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        sumup = 0
        diff = 1000000
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                sumup = nums[i] + nums[l] + nums[r]
                if sumup == target:
                    return target
                elif sumup < target:
                    l += 1
                elif sumup > target:
                    r -= 1
                if abs(sumup - target) < diff:
                    diff = abs(sumup - target)
                    result = sumup
        return result
    
