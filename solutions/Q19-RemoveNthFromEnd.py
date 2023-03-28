from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head # prev is n+1 nodes behind curr
        curr = prev # curr is n nodes behind prev

        if (head.next is None): # if there is only one node
            return None # return None

        # move curr n nodes ahead
        for _ in range(n): 
            curr = curr.next

        # if curr is None, then we need to remove the head
        if (curr is None):
            head = head.next
            return head
        
        # move prev and curr until curr is at the end
        while curr.next is not None:
            prev = prev.next
            curr = curr.next
        
        # remove the node after prev
        prev.next = prev.next.next

        return head