# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        # left root right
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # submit accept

        # RECURSIVE
        # res = []
        #
        # def recursive_inorder(root):
        #     if not root:
        #         # if root is none return none
        #         return
        #     recursive_inorder(root.left)
        #     # do check all the left subTreeNode to do the recursive inorder
        #     res.append(root.val)
        #     # after left then push the root.val into the res
        #     recursive_inorder(root.right)
        #     # check all the right subTreeNode to do recursive inorder again
        #
        #     return res
        #
        # return recursive_inorder(root)

        # ITERATION
        res = []
        stack = []
        # store the root of treeNode
        curr = root

        while curr or stack:
            while curr:
                # loop to store the left subTreeNode root until there is no root.left
                stack.append(curr)
                # do not need to push the curr.val since we need to store the root of the treeNode
                curr = curr.left
            # stack should be all the left subTreeNode root and the original root
            curr = stack.pop()
            # update the curr to the current root
            res.append(curr.val)
            # push the curr.val to the res
            curr = curr.right
            # have to update the curr to the curr.right to back to the loop to check if there is right subTreeNode

        # after the while loop we should complete the inorder Traversal
        return res
