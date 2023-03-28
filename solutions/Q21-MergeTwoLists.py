from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: # if list1 is empty
            return list2 # return list2

        if list2 is None: # if list2 is empty
            return list1 # return list1

        if list1.val < list2.val: # if list1's value is less than list2's value
            list1.next = self.mergeTwoLists(list1.next, list2) # set list1's next to the result of the recursive call
            return list1 # return list1
        else: # if list2's value is less than list1's value
            list2.next = self.mergeTwoLists(list1, list2.next) # set list2's next to the result of the recursive call
            return list2 # return list2