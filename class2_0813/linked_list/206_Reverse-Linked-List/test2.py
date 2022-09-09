# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        next_Node = None

        while curr is not None:
            next_Node = curr.next
            curr.next = prev

            prev = curr
            curr = next_Node

        return prev
