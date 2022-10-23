class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        val = 0
        sign = 1
        for n in s:
            if (not n.isspace()):
                break
            elif (n.isspace()):
                i +=1
    
        s = s[i:]
    
        for n in s:
            if n.isalpha():
                return 0
            break
        i = 0
        for n in s:
            if (n == "-"):
                sign *= -1
                i +=1
            elif (n == '+'):
                i += 1
            break
    
        d = 0
        v = i
        for n in s:
            if (n.isdigit()):
                val = val*10 + ord(n) - 48
                v += 1
            elif (n == '.' or n.isalpha() or (d != 0 and (n == '-' or n == '+'))):
                break
            if (not n.isspace()):
                d +=1
            elif (n.isspace() and v >= 1):
                break
        
        if (val * sign > 2147483647):
            return 2147483647
        elif (val * sign < -2147483648):
            return -2147483648
        return val * sign
        