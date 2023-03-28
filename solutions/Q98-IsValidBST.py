from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, arr):
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        treeList = []
        self.inorder(root, treeList)
        return treeList == sorted(treeList)
