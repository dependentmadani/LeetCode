class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_convert = ['' for i in range(numRows)]
        n = 0
        direction = 1
        for i in s:
            new_convert[n] += i
            if (n == numRows - 1):
                direction = 0
            elif (n == 0):
                direction = 1
            if direction == 1:  #if direction is down
                n += 1
            elif direction == 0: #if direction is up
                n -= 1
        return ''.join(new_convert)
        