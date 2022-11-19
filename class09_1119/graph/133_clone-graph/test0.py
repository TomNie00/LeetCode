"""
# Definition for a Node.

"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        oldToNew = {}

        def workhorse(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]

            copy_node = Node(node.val)
            oldToNew[node] = copy_node

            for neib in node.neighbors:
                copy_node.neighbors.append(workhorse(neib))

            return copy_node

        return workhorse(node)
