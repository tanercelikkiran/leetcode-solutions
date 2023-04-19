from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0

        ans = 0

        def dfs(node, direction):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left, False)
            right = dfs(node.right, True)
            ans = max(ans, left, right)
            return 1 + (left if direction else right)

        dfs(root, False)

        return ans