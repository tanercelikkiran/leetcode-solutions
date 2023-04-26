from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [] 
        q.append(root)

        while q:
            sub_ans = []
            for _ in range(len(q)):
                node = q.pop()
                sub_ans.append(node.val)
                if node.left:
                    q.insert(0, node.left)
                if node.right:
                    q.insert(0, node.right)
            ans.append(sub_ans)

        return ans

print(Solution().levelOrder())


