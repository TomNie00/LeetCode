# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class newTreeNode:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # Function to insert nodes in level order
# def insertLevelOrder(arr, i, n):
#     root = None
#
#     if i < n:
#         root = newTreeNode(arr[i])
#
#         root.left = insertLevelOrder(arr, 2 * i + 1, n)
#         root.right = insertLevelOrder(arr, 2 * i + 2, n)
#
#     return root


import collections


class Solution(object):

    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """

        root.parent = None
        self.buildParents(root)


        # node_dict = collections.defaultdict(list)
        q = collections.deque()
        start_node = self.findNode(start, root)

        # print(start_node.val)
        # print("h")

        q.append(start_node)
        visit =[start_node]
        time = 0

        while q:
            size = len(q)
            while size:
                size -= 1
                curr_node = q.popleft()
                print("curr_node: ", curr_node.val)
                if curr_node.parent and curr_node.parent not in visit:
                    visit.append(curr_node.parent)
                    q.append(curr_node.parent)
                if curr_node.left and curr_node.left not in visit:
                    visit.append(curr_node.left)
                    q.append(curr_node.left)
                if curr_node.right and curr_node.right not in visit:
                    visit.append(curr_node.right)
                    q.append(curr_node.right)

            if len(q) == 0:
                return time
            else:
                time += 1




    def findNode(self, start, root):
        if root is None:
            return None

        if root.val == start:
            return root


        res = self.findNode(start, root.left)
        if res is not None:
            return res
        else:
            return self.findNode(start, root.right)


    def buildParents(self, root):
        if not root:
            return None
        if root.left:
            root.left.parent = root
        if root.right:
            root.right.parent = root

        self.buildParents(root.left)
        self.buildParents(root.right)


def buildBinaryTree(int_list):
    node_list = []

    for i in int_list:
        if i:
            curr_node = TreeNode(i)
            node_list.append(curr_node)
        else:
            node_list.append(None)
    for idx in range(len(node_list)):
        if not node_list[idx]:
            continue
        if 2*idx + 1 < len(node_list) and node_list[2*idx + 1]:
            node_list[idx].left = node_list[2*idx + 1]
        if 2*idx + 2 < len(node_list) and node_list[2*idx + 2]:
            node_list[idx].right = node_list[2*idx + 2]

    return node_list[0]




def bfs(root):
    q = collections.deque()
    q.append(root)

    while q:
        size = len(q)
        level = []
        while size:
            size -= 1
            curr_node = q.popleft()
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            level.append(curr_node.val)

        print("level: ", level)


if __name__ == '__main__':
    # root = [1, 5, 3, None, 4, 10, 6, None, None, 9, 2]
    # start = 3
    #
    #
    #
    # root = buildBinaryTree(root)
    # # bfs(root)
    # obj = Solution()
    #
    #
    #
    # res = obj.amountOfTime(root,start)
    #
    # print("final res: ", res)
    #
    # root = [1]
    # start = 1
    #
    # root = buildBinaryTree(root)
    #
    #
    # obj = Solution()
    #
    # res = obj.amountOfTime(root, start)
    #
    # print("final res: ", res)

    root = [1, None, 2, None, 3, None, 4, None, 5]
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.right = node2
    node2.right = node3
    node3.right = node4
    node4.right = node5

    start = 2

    root = node1
    bfs(root)

    obj = Solution()

    res = obj.amountOfTime(root, start)

    print("final res: ", res)



