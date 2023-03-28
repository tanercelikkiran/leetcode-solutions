class Solution:
    def intToRoman(self, num: int) -> str:
        ans = "" # answer
        # while num is not 0 (num is not equal to 0) 
        while num != 0:
            # reduce num by its largest roman numeral equivalent and add it to ans
            if (num >= 1000):
                ans += "M"
                num -= 1000
            elif (num >= 900):
                ans += "CM" 
                num -= 900
            elif (num >= 500):
                ans += "D"
                num -= 500
            elif (num >= 400):
                ans += "CD"
                num -= 400
            elif (num >= 100):
                ans += "C"
                num -= 100
            elif (num >= 90):
                ans += "XC"
                num -= 90
            elif (num >= 50):
                ans += "L"
                num -= 50
            elif (num >= 40):
                ans += "XL"
                num -= 40
            elif (num >= 10):
                ans += "X"
                num -= 10
            elif (num >= 9):
                ans += "IX"
                num -= 9
            elif (num >= 5):
                ans += "V"
                num -= 5
            elif (num >= 4):
                ans += "IV"
                num -= 4
            else:
                ans += "I"
                num -= 1
        return ans