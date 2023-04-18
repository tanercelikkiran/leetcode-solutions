from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root or (not root.left and not root.right):
            return
        
        def inorder(node):
            if node:
                inorder(node.left)
                stack.append(node)
                inorder(node.right)

        stack = []

        inorder(root)

        node1 = node2 = None

        for i in range(len(stack) - 1):
            if stack[i].val > stack[i + 1].val:
                node1 = stack[i]
                break
        for i in range(len(stack) - 1, 0, -1):
            if stack[i].val < stack[i - 1].val:
                node2 = stack[i]
                break

        node1.val, node2.val = node2.val, node1.val

Solution().recoverTree(TreeNode(1, TreeNode(3, None, TreeNode(2))))