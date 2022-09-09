# Definition for singly-linked list.
from class3_0827.linked_list.utils import ListNode
from class3_0827.linked_list.utils import build_list, display


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        meet = False

        if head is None:
            return None

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = True
                break

        if meet:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next

            return fast
        else:
            return None

if __name__ == '__main__':
    # vals = [0, 1, 2, 3, 4, 5, 6]
    # head = build_list(vals, [[6,2]])
    # display(head)
    # obj = Solution()
    # print('*********\n')
    # res = obj.detectCycle(head)
    # print(res)

    # vals = [3,2,0,-4]
    # head = build_list(vals, [[3 , 1]])
    # display(head)
    # obj = Solution()
    # print('*********\n')
    # res = obj.detectCycle(head)
    # print(res)

    vals = [1, 2]
    head = build_list(vals, [[1, 0]])
    display(head)
    obj = Solution()
    print('*********\n')
    res = obj.detectCycle(head)
    print(res)
