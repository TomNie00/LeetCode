"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while curr is not None:
            if curr.child:
                tail = curr.child

                while tail.next is not None:
                    tail = tail.next

                tail.next = curr.next

                if curr.next is not None:
                    curr.next.prev = tail

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            else:
                curr = curr.next

        return head
