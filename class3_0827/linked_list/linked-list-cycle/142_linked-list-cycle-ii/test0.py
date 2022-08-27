# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        meet = False
        while fast.next.next and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = True
                break
        if meet:
            fast = head
            if fast == slow:
                return fast
            else:
                fast = fast.next
                slow = slow.next
        else:
            return None
