
class Solution:

    
    def longestPalindrome(self, s: str) -> str:
        LongPal = ""
        len_longPal = 0
        
        for i in range(len(s)):
            left , right = i, i
            new = ""
            new, left, right,len_longPal = self.check_palindrom(s, left, right,len_longPal)
            if (new != ""):
                LongPal = new
            
            left, right = i, i + 1
            new = ""
            new, left, right,len_longPal = self.check_palindrom(s, left, right,len_longPal)
            if (new != ""):
                LongPal = new
        
        return LongPal
    
    def check_palindrom(self, s:str, left:int, right:int, len_longPal:int):
        LongPal = ""
        
        while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > len_longPal):
                    LongPal = s[left: right + 1]
                    len_longPal = right - left + 1
                left -= 1
                right += 1
        return LongPal, left, right, len_longPal