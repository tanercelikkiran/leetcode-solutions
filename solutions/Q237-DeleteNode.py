# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next is not None: # while the next node is not the last node
            node.val = node.next.val # set the current node's value to the next node's value
            node = node.next # move to the next node
        node.val = node.next.val # set the current node's value to the next node's value
        node.next = None # set the next node to None