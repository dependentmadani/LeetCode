import numpy
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = []
        np_array = numpy.array(nums)
        result = [item for item, count in Counter(np_array).items() if (count > 1)]
        if (result == []):
            return False
        else:
            return True
