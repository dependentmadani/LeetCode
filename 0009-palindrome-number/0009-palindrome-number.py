class Solution:
    def isPalindrome(self, x: int) -> bool:
        main_x = x
        reversed_x = 0
        reminder = 0
        
        while (int(x)):
            reminder = int(x % 10)
            reversed_x = reversed_x * 10 + reminder
            x /= 10

        if main_x == reversed_x:
            return True
        else:
            return False