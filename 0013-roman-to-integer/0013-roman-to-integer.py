class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        while s != "":
            if s.count("IV"):
                result += 4 * s.count("IV")
                s = s.replace("IV", "")
            elif s.count("IX"):
                result += 9 * s.count("IX")
                s = s.replace("IX", "")
            elif s.count("XL"):
                result += 40 * s.count("XL")
                s = s.replace("XL", "")
            elif s.count("XC"):
                result += 90 * s.count("XC")
                s = s.replace("XC", "")
            elif s.count("CD"):
                result += 400 * s.count("CD")
                s = s.replace("CD", "")
            elif s.count("CM"):
                result += 900 * s.count("CM")
                s = s.replace("CM", "")
            elif s.count("I"):
                result += 1 * s.count("I")
                s = s.replace("I", "")
            elif s.count("V"):
                result += 5 * s.count("V")
                s = s.replace("V", "")
            elif s.count("X"):
                result += 10 * s.count("X")
                s = s.replace("X", "")
            elif s.count("L"):
                result += 50 * s.count("L")
                s = s.replace("L", "")
            elif s.count("C"):
                result += 100 * s.count("C")
                s = s.replace("C", "")
            elif s.count("D"):
                result += 500 * s.count("D")
                s = s.replace("D", "")
            elif s.count("M"):
                result += 1000 * s.count("M")
                s = s.replace("M", "")
        return result