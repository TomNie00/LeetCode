# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        addr = []

        while head.next is not None:
            for i in range(len(addr)):
                if id(head.val) == addr[i]:
                    return True
            addr.append(id(head.val))

        return False
