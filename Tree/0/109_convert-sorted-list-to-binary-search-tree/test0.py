# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # submit accept

        # SLOW AND FAST POINTER
        # if not head:
        #     return None
        # if not head.next:
        #     return TreeNode(head.val)
        # # we need to return a treenode since our rtype is treenode
        #
        # slow = fast = head
        # pre = None
        # # using the pre to store the linklist before the mid
        # while fast and fast.next:
        #     # using slow and fast to find the mid in the linklist
        #     pre = slow
        #     slow = slow.next
        #     fast = fast.next.next
        #
        # pre.next = None
        # # cut the linklist before the mid
        #
        # root = TreeNode(slow.val)
        # root.left = self.sortedListToBST(head)
        # root.right = self.sortedListToBST(slow.next)
        #
        # return root

        # CHANGE THE LINKLIST INTO LIST
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def helper(nums):
            if not nums:
                return None
            nums_length = len(nums)
            mid = nums_length // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid + 1:])
            return root
        return helper(nums)