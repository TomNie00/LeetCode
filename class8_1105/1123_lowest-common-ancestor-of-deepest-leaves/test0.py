# BUILD A TREE BY ARRAY
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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def find_lca_2_nodes(self, node1, node2):
        node1_ac = [node1]
        node2_ac = [node2]

        while node1.parent:
            node1_ac.append(node1.parent)
            node1 = node1.parent
        while node2.parent:
            node2_ac.append(node2.parent)
            node2 = node2.parent
        node1_ac.reverse()
        node2_ac.reverse()
        # print('>>>')
        # for a in node1_ac:
        #     print(a.val)
        # print('>>>')
        # for a in node2_ac:
        #     print(a.val)

        i = 0
        while i < min(len(node1_ac), len(node2_ac)):
            if i + 1 >= len(node1_ac) or i + 1 >= len(node2_ac):
                return node1_ac[i]
            if node1_ac[i + 1] != node2_ac[i + 1]:
                return node1_ac[i]
            i += 1
        print('Error')

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root.parent = None
        self.build_parent_link(root)
        deepest_nodes = self.get_deepest_nodes(root)
        if len(deepest_nodes) == 1:
            return deepest_nodes[0]
        print('deepest_nodes: ', len(deepest_nodes))
        while len(deepest_nodes) > 1:
            l1 = deepest_nodes.pop(0)
            l2 = deepest_nodes.pop(0)
            cur_ac = self.find_lca_2_nodes(l1, l2)
            deepest_nodes.append(cur_ac)
        return deepest_nodes[0]

    def build_parent_link(self, node):
        if node is None:
            return
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node
        self.build_parent_link(node.left)
        self.build_parent_link(node.right)

    def get_deepest_nodes(self, root):
        level_dict = {}
        self.mark_levels(root, 0, level_dict)
        keys_len = len(level_dict.keys())
        deepest_nodes = level_dict[keys_len - 1]
        return deepest_nodes

    def mark_levels(self, node, cur_dept, level_dict):
        if node is None:
            return
        if cur_dept not in level_dict:
            level_dict[cur_dept] = []
        level_dict[cur_dept].append(node)
        self.mark_levels(node.left, cur_dept + 1, level_dict)
        self.mark_levels(node.right, cur_dept + 1, level_dict)


