class Solution:
    def longestPalindrome(self, s: str) -> str:
        LongPal = ""
        len_longPal = 0
        
        for i in range(len(s)):
            left , right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > len_longPal):
                    LongPal = s[left: right + 1]
                    len_longPal = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > len_longPal):
                    LongPal = s[left: right + 1]
                    len_longPal = right - left + 1
                left -= 1
                right += 1
        
        return LongPal