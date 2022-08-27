# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        vls = []

        while head is not None:
            vls.append(head.val)
            head = head.next


        i = 0
        j = len(vls) - 1

        while i < j:
            if vls[i] != vls[j]:
                return False
            else:
                i += 1
                j -= 1

        return True