from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return

        n = 1

        curr = head

        while curr.next != None:
            curr = curr.next
            n += 1

        curr.next = head

        curr = head

        k %= n

        for _ in range(n-k-1):
            curr = curr.next
        
        head = curr.next
        curr.next = None

        return head