class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: # if there is no head or head.next, then
            return head # return head
        new_head = head.next # set new_head to head.next
        head.next = self.swapPairs(new_head.next) # set head.next to the result of the recursive call
        new_head.next = head # set new_head.next to head
        return new_head