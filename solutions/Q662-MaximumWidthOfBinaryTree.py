from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 1 # answer
        q = deque() # queue
        q.append((root, 1)) # add root node
        while q: # while queue is not empty
            ans = max(ans, q[-1][1] - q[0][1] + 1) # update answer with max width
            for _ in range(q.__len__()): # for each node in the queue
                node, index = q.popleft() # pop node and index
                if node.left is not None: # if left child exists
                    q.append((node.left, index * 2)) # add left child to queue
                if node.right is not None: # if right child exists
                    q.append((node.right, index * 2 + 1)) # add right child to queue
        return ans