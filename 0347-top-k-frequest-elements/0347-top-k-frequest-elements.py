class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        result = []
        number_elements = []
        i = 0
        while (i < len(nums)):
            counter = nums.count(nums[i])
            # if (counter >= k):
            result.append(nums[i])
            number_elements.append(counter)
            i += counter
        output = []
        while (k != 0):
            highest_value = 0
            index = 0
            i = 0
            while (i < len(number_elements)):
                if (highest_value < number_elements[i]):
                    highest_value = number_elements[i]
                    index = i
                i += 1
            output.append(result[index])
            number_elements.pop(index)
            result.pop(index)
            k -= 1
            
        return output
