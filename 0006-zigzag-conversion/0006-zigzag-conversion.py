class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_convert = ['' for i in range(numRows)]
        n = 0
        direction = 'down'
        for i in s:
            new_convert[n] += i
            if (n == numRows - 1):
                direction = 'up'
            elif (n == 0):
                direction = 'down'
            if direction == 'down':
                n += 1
            elif direction == 'up':
                n -= 1
        return ''.join(new_convert)
        