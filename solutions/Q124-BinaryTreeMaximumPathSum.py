from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> Tuple[int, int]:
            if node is None:
                return (float("-inf"), 0)
            left_max, left_sum = dfs(node.left)
            right_max, right_sum = dfs(node.right)
            max_sum = max(left_max, right_max, left_sum + node.val + right_sum)
            sum = max(left_sum + node.val, right_sum + node.val, 0)
            return (max_sum, sum)
        return dfs(root)[0]