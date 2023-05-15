from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1 = node2 = head

        for i in range(k-1):
            node1 = node1.next

        temp = node1

        while temp.next:
            node2 = node2.next
            temp = temp.next

        temp = node1.val
        node1.val = node2.val
        node2.val = temp

        return head