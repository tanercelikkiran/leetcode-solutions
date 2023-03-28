from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # if head is None,
            return None # return None
        dummy = ListNode(0, head) # create a dummy node with value 0 and next node as head (for the case when head is the first node to be deleted)
        prev = dummy # set prev to dummy
        while head: # while head is not None
            if head.next and head.val == head.next.val: # if element is duplicate
                while head.next and head.val == head.next.val: # while element is duplicate
                    head = head.next # move head to next node
                prev.next = head.next # set prev.next to head.next (to skip the duplicate nodes)
            else: # if element is not duplicate
                prev = prev.next # move prev to next node
            head = head.next # move head to next node
        return dummy.next # return dummy.next (the head of the linked list)