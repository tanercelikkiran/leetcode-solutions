class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = "aeiou" # create a string of vowels

        s = list(s) # convert string to list

        i = 0 # index of first character
        j = len(s) - 1 # index of last character

        while i < j: # while i is less than j
            if s[i].lower() not in vowel: # if the character at index i is not a vowel
                i += 1 # increment i
            elif s[j].lower() not in vowel: # if the character at index j is not a vowel     
                j -= 1 # decrement j
            else: # if both characters are vowels
                s[i], s[j] = s[j], s[i] # swap the characters
                i += 1 # increment i
                j -= 1 # decrement j

        return "".join(s) # convert list back to string