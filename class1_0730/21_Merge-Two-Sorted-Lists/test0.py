# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        cur = new = ListNode(0)

        if list1 == 0 or list2 == 0:
            if list1 == 0:
                cur.next = list2
            else:
                cur.next = list1

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        return new.next


if __name__ == "__main__":
    obj = Solution()

    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    result = ListNode(0)

    result.next = obj.mergeTwoLists(list1, list2)

    print(result.next)
