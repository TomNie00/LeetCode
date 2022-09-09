# Definition for singly-linked list.
from class3_0827.linked_list.utils import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        if head is None:  # 如果head为空直接return
            return False

        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False

        while fast.next and fast.next.next: # 这个要比上面的快
            fast = fast.next
            if fast == slow:
                return True
            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
        return False
