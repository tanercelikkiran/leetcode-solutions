class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        # Explanation:
        # (s+s) is a string that contains 2 copies of s, e.g. s="ab", (s+s)="abab"
        # [1:-1] is a slice that gets rid of the first and last character, e.g. "bab"
        # s in (s+s)[1:-1] checks if s is contained in (s+s)[1:-1], e.g. "ab" in "bab"
        # If s is contained in (s+s)[1:-1], then s is a repeated substring pattern
        # If s is not contained in (s+s)[1:-1], then s is not a repeated substring pattern
        # This is because if s is a repeated substring pattern, then (s+s) will contain
        # at least 2 copies of s, and removing the first and last character will still
        # contain at least 1 copy of s, which is why s is contained in (s+s)[1:-1]