from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            ld = get_depth(root.left)
            rd = get_depth(root.right)
            
            if ld == -1 or rd == -1:
                return -1

            if abs(ld - rd) > 1:
                return -1
            
            return 1 + max(ld, rd)
        
        return get_depth(root) != -1