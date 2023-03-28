from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode() # dummy head 
        ans_tail = ans # tail of the answer
        carry = 0 # carry
        while l1 or l2 or carry: # while there are still nodes to process or carry
            if l1: # if l1 is not None
                carry += l1.val # add l1.val to carry
                l1 = l1.next # move l1 to the next node
            if l2: # if l2 is not None
                carry += l2.val # add l2.val to carry
                l2 = l2.next # move l2 to the next node
            ans_tail.next = ListNode(carry % 10) # add the last digit of carry to the answer
            ans_tail = ans_tail.next # move ans_tail to the next node
            carry //= 10 # remove the last digit of carry
        return ans.next