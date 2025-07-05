#solution 1: O(N)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyNumber = -1
        checkedNumbers = []

        for i in arr:
            if i not in checkedNumbers:
                numberCounter = arr.count(i)
                if i == numberCounter:
                    if i > luckyNumber:
                        luckyNumber = i
                    checkedNumbers.append(i)

        return luckyNumber


#solution 2: O(NlogN)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)

        checkedNumber = []
        for i in arr:
            if i not in checkedNumber:
                checkedNumber.append(i)
                numberCounter = arr.count(i)
                if i == numberCounter:
                    return i

        return -1