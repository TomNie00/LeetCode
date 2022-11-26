import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def buildBinaryTree(int_list):
#     node_list = []
#
#     for i in int_list:
#         if i:
#             curr_node = TreeNode(i)
#             node_list.append(curr_node)
#         else:
#             node_list.append(None)
#     for idx in range(len(node_list)):
#         if not node_list[idx]:
#             continue
#         if 2 * idx + 1 < len(node_list) and node_list[2 * idx + 1]:
#             node_list[idx].left = node_list[2 * idx + 1]
#         if 2 * idx + 2 < len(node_list) and node_list[2 * idx + 2]:
#             node_list[idx].right = node_list[2 * idx + 2]
#
#     return node_list[0]

# def insertLevelOrder(arr, i, n):
#     root = None
#
#     if i < n:
#         root = TreeNode(arr[i])
#
#         root.left = insertLevelOrder(arr, 2 * i + 1, n)
#         root.right = insertLevelOrder(arr, 2 * i + 2, n)
#
#     return root

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

def deserialize(int_array):
    if len(int_array) == 0:
        return []
    nodes = [None if val == 'null' or val is None else TreeNode(val)
             for val in int_array]

    kids = nodes[1::][::-1]

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return nodes[0]

if __name__ == '__main__':

    root = [1,None,2,None,3,None,4,None,5]
    # root = []
    # root1 = buildBinaryTree(root)
    # root2 = insertLevelOrder(root, 0, len(root))
    root3 = deserialize(root)
    # print(bfs(root3))