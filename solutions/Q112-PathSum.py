from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # if root is None
            return False # return False
        if not root.left and not root.right: # if root.left is None and root.right is None
            return targetSum == root.val # return targetSum == root.val
        # return that the targetSum - root.val is equal to the left or right subtree
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val) 