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

        vls = []
        while head is not None:
            vls.append(head.val)
            head = head.next

        vls.reverse()

        ahead = None
        tail = None

        for i in range(len(vls)):
            cur_node = ListNode()
            cur_node.val = vls[i]
            if tail is not None:
                tail.next = cur_node
                tail = cur_node
            else:
                tail = cur_node
                ahead = cur_node

        return ahead




