from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge sort algorithm

        # Base case
        if head is None or head.next is None:
            return head
        
        # Find the middle node
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        mid = slow.next
        slow.next = None

        return self.merge(self.sortList(head), self.sortList(mid))