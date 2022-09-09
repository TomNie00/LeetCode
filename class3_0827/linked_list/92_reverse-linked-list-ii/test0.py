from class3_0827.linked_list.utils import ListNode
from class3_0827.linked_list.utils import build_list, display



class Solution(object):

    def reverse(self,head):
        prev = None
        curr = head
        new_tail = head

        while curr is not None:
            new_node = curr.next
            curr.next = prev

            prev = curr
            curr = new_node

        return prev,new_tail

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # vls = []
        # while head is not None:
        #     vls.append(head.val)
        #     head = head.next
        # subarr = vls[left - 1:right]
        # subarr = subarr[::-1]
        #
        # newarr = vls[:left - 1] + subarr + vls[right:]
        #
        # ahead = None
        # tail = None
        #
        # for i in range(len(newarr)):
        #     cur_node = ListNode()
        #     cur_node.val = newarr[i]
        #     if tail is not None:
        #         tail.next = cur_node
        #         tail = cur_node
        #     else:
        #         tail = cur_node
        #         ahead = cur_node
        #
        # return ahead

        curr = head
        ahead = head
        atail = head
        index = 1
        dummy_head = ListNode(0)
        dummy_head.next = head

        while index < left:
            curr = curr.next
            ahead = ahead.next
            atail = atail.next
            


