class Solution:
    def reverse(self, x: int) -> int:
        val = str(x)
        reversed_val = 0
        sign = 1
        if (x < 0):
            sign = -1
            val = self.reversed_str(val)
        else:
            val = val[::-1]
        reversed_val = int(val) * sign
        if (reversed_val < -2**(31) or reversed_val > (2**(31) - 1)):
            return 0
        return reversed_val
    
    def reversed_str(self, text: str):
        if len(text) <= 1:
            return ""
        else:
            return text[-1] + self.reversed_str(text[:-1])
