from typing import List

from class3_0827.linked_list.utils import ListNode
from class3_0827.linked_list.utils import build_list, display

class Solution(object):
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

        if head is None or left == right:
            return head

        dummyhead = ListNode(0)
        dummyhead.next = head
        curr = head
        ahead = None
        sechead = None
        atail = None
        sectail = None
        prev = None
        index = 1

        while curr is not None:
            if index == left - 1:
                ahead = curr
                sechead = curr.next

            if index == right:
                if curr.next is not None:
                    sectail = curr.next
                    atail = curr
            else:
                atail = curr

            curr = curr.next
            index += 1

        # 开始反转从left到right的节点
        curr = sechead
        while curr != sectail:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # 将反转之后的节点进行拼接
        ahead.next = atail
        sechead.next = sectail
        return dummyhead.next


if __name__ == '__main__':
    obj = Solution()
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    print('*********\n')
    res = obj.reverseBetween(head, left, right)
    print(res)




