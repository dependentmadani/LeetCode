class Solution:
    def processStr(self, s: str) -> str:
        characters = ""
        result = ""

        for i in s:
            if i == "*" or i == "#" or i == "%":
                if i == "*":
                    result = result[:-1]
                elif i == "#":
                    result += result
                else:
                    result = result[::-1]
            else:
                result += i
        
        return result