class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 # answer
        # create a dictionary of roman numerals and their values
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        while s:
            # if the first two characters of s are in the dictionary
            if s[:2] in roman:
                # add the value of the first two characters to ans
                ans += roman[s[:2]]
                # remove the first two characters from s
                s = s[2:]
            # if the first character of s is in the dictionary
            elif s[0] in roman:
                # add the value of the first character to ans
                ans += roman[s[0]]
                # remove the first character from s
                s = s[1:]
        return ans