# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from class3_0827.linked_list.utils import ListNode
from class3_0827.linked_list.utils import build_list, display

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        addr = {}
        index = 0
        while head is not None:
            if id(head) in addr:
                print(addr)
                return True
            addr[id(head)] = index
            head = head.next
            index += 1

        return False

# def build_list(node_vals, edges):
#     nodes = []
#     for v in node_vals:
#         nodes.append(ListNode(v))
#
#     for i in range(0, len(node_vals)-1):
#         nodes[i].next = nodes[i+1]
#
#     for e in edges:
#         nodes[e[0]].next = nodes[e[1]]
#     return nodes[0]
#
#
# def display(head):
#     cnt = 10
#     while head:
#         print(head.val)
#         head = head.next
#         cnt -= 1
#         if cnt <= 0:
#             break

if __name__ == '__main__':
    vals = [3, 2, 0, -4]
    head = build_list(vals, [[3,0]])
    display(head)
    obj = Solution()
    res = obj.hasCycle(head)
    print(res)