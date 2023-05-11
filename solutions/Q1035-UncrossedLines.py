from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        commonElements = set(nums1) & set(nums2)

        if len(commonElements) == 0:
            return 0

        nums1 = list(filter(lambda k: k in commonElements, nums1))
        nums1.reverse()
        nums2 = list(filter(lambda k: k in commonElements, nums2))
        nums2.reverse()

        n, m = len(nums1), len(nums2)

        dp = [[0]*(m+1) for _ in range(+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]