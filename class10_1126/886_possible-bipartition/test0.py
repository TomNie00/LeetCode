import collections


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        dislike_dict = collections.defaultdict(list)

        which_group = {i: None for i in range(1, n + 1)}

        for a, b in dislikes:
            dislike_dict[a].append(b)
            dislike_dict[b].append(a)

        def workhorse(node, group):
            if not which_group[node]:
                which_group[node] = group
            else:
                return which_group[node] == group

            for value in dislike_dict[node]:
                if not workhorse(value, 2 if group == 1 else 1):
                    return False

            return True

        for i in range(1, n + 1):
            if not which_group[i] and not workhorse(i, 1):
                return False

        return True


if __name__ == '__main__':
    object = Solution()

    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]

    print(object.possibleBipartition(n, dislikes))
