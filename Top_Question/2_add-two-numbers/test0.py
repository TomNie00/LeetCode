# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # submit accept

        res = ListNode()
        curr = res
        carry = 0
        while l1 or l2 or carry:
            # make sure every carry or Listnode is 0 or empty
            if l1:
                l3 = l1.val
                l1 = l1.next
            else:
                l3 = 0
            if l2:
                l4 = l2.val
                l2 = l2.next
            else:
                l4 = 0

            numSum = l3 + l4 + carry
            # get the sum of three values
            num = numSum % 10
            # get the last digit of the sum and will put in to Listnode
            carry = numSum // 10
            # get the carry for next operation

            curr.next = ListNode(num)
            curr = curr.next

        return res.next

if __name__ == '__main__':
    object = Solution()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    res = object.addTwoNumbers(l1,l2)

    print(res)
