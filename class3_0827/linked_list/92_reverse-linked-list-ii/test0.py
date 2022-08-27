# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        vls = []
        while head is not None:
            vls.append(head.val)
            head = head.next

        if right - left == 0:
            return head
        elif (right - left) % 2 == 0:
            times = (right - left) / 2
        else:
            times = (right - left) / 2 + 1

        nums = 0
        while nums < times:
            temp = vls[left - 1]
            vls[left - 1] = vls[right - 1]
            vls[right - 1] = temp

            left += 1
            right -= 1
            nums += 1

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
