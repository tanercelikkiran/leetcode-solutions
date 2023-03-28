from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 # index for nums1
        j = 0 # index for nums2
        while i < m and j < n: # iterate through both lists
            if nums1[i] > nums2[j]: # if the current element in nums1 is greater than the current element in nums2
                nums1.insert(i, nums2[j]) # insert the current element in nums2 into nums1
                nums1.pop() # remove the last element in nums1
                j += 1 # increment the index for nums2
                m += 1 # increment the index for nums1
            i += 1 # increment the index for nums1
        while j < n: # if there are still elements in nums2
            nums1[i] = nums2[j] # add the remaining elements in nums2 to nums1
            i += 1 # increment the index for nums1
            j += 1 # increment the index for nums2