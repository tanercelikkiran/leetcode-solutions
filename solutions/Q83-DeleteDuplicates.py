from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None): # if head is None or head.next is None, then
            return head # return head

        temp = head # set temp to head
        curr = head.next; # set curr to head.next

        while curr is not None: # while curr is not None
            if (curr.val == temp.val): # if curr.val == temp.val
                temp.next = curr.next # set temp.next to curr.next
                curr = temp.next # set curr to temp.next
            else: # else
                temp = curr # set temp to curr
        
        return head