from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # key: sorted string, value: list of anagrams
        for s in strs: # for each string
            key = "".join(sorted(s)) # sort the string and convert to string
            if key in d: # if the key exists
                d[key].append(s) # append the string to the list
            else: # if the key does not exist
                d[key] = [s] # create a new key-value pair
        return list(d.values())