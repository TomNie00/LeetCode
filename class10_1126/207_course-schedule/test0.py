import collections


class Node(object):
    def __init__(self, val=0, is_prerequisite_of=None):
        self.val = val
        self.is_prerequisite_of = is_prerequisite_of if is_prerequisite_of is not None else []
        self.is_advance_of = []


class Solution(object):
    def find_no_prereq(self, prerequire_dict, visited):
        for i in prerequire_dict:
            node = prerequire_dict[i]
            if node in visited:
                continue

            if len(node.is_advance_of) == 0:
                visited.append(node)
                return node

        return None



    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """



        prerequire_dict = collections.defaultdict()
        no_advance_course = []

        for i in range(numCourses):
            prerequire_dict[i] = Node(i)

        for course, pre in prerequisites:
            if course == pre:
                return False
            prerequire_dict[pre].is_prerequisite_of.append(prerequire_dict[course])
            prerequire_dict[course].is_advance_of.append(prerequire_dict[pre])

        visited = []

        while len(visited) != numCourses:
            res = self.find_no_prereq(prerequire_dict,visited)

            if res is None:
                return False

            for next_level in res.is_prerequisite_of:
                next_level.is_advance_of.remove(res)

        return True




    def bfs(self, node):
        if node in self.visited:
            return True
        q = collections.deque()
        q.append(node)

        while q:
            size = len(q)
            cur_layer_visited = []
            while size:
                size -= 1
                curr_node = q.popleft()
                for i in curr_node.is_prerequisite_of:
                    if i in self.visited:
                        return False
                    else:
                        cur_layer_visited.append(i)
                        q.append(i)
            self.visited.extend(cur_layer_visited)

        return True

    def dfs(self, node, curr_visited):
        if node in curr_visited:
            return False
        if node in self.visited:
            return True

        self.visited.append(node)
        curr_visited.append(node)

        for i in node.is_prerequisite_of:
            if self.dfs(i,curr_visited) is False:
                return False

        curr_visited.pop()

        return True



if __name__ == '__main__':
    object = Solution()

    numCourses = 3
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    print(object.canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[1, 0],[0,1]]

    print(object.canFinish(numCourses,prerequisites))
    #
    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    print(object.canFinish(numCourses, prerequisites))
    #
    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

    print(object.canFinish(numCourses, prerequisites))








