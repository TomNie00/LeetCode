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
        if head is None or left == right:
            return head

        dummyhead = ListNode(0, head)
        dummyhead.next = head
        curr = head
        ahead = None
        sechead = None
        atail = None
        sectail = None
        prev = None
        index = 0
        
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
            # 事先保存cur的下一个节点
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # 将反转之后的节点进行拼接
        ahead.next = atail
        sechead.next = sectail
        return dummyhead.next


if __name__ == '__main__':
    obj = Solution()
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    res = obj.reverseBetween(head, left, right)
    print(res)
