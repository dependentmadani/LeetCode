class Solution:
    def intToRoman(self, num: int) -> str:
        initial = 0
        result = ""
        while num > 0:
            if num < 1000 and num >= 900:
                result += "CM"
                num -= 900
            elif num < 500 and num >= 400:
                result += "CD"
                num -= 400
            elif num < 100 and num >= 90:
                result += "XC"
                num -= 90
            elif num < 50 and num >= 40:
                result += "XL"
                num -= 40
            elif num == 9:
                result += "IX"
                num -= 9
            elif num == 4:
                result += "IV"
                num -= 4
            if num - 1000 >= 0 and not self.check_special_condition(num):
                result += 'M'
                num -= 1000
            elif num - 500 >= 0 and not self.check_special_condition(num):
                result += 'D'
                num -= 500
            elif num - 100 >= 0 and not self.check_special_condition(num):
                result += 'C'
                num -= 100
            elif num - 50 >= 0 and not self.check_special_condition(num):
                result += 'L'
                num -= 50
            elif num - 10 >= 0 and not self.check_special_condition(num):
                result += 'X'
                num -= 10
            elif num - 5 >= 0 and not self.check_special_condition(num):
                result += 'V'
                num -= 5
            elif num - 1 >= 0 and not self.check_special_condition(num):
                result += 'I'
                num -= 1
        return result
    
    def check_special_condition(self, num: int):
        if num < 1000 and num >= 900:
            return True
        elif num < 500 and num >= 400:
            return True
        elif num < 100 and num >= 90:
            return True
        elif num < 50 and num >= 40:
            return True
        elif num == 9:
            return True
        elif num == 4:
            return True
        return False
    