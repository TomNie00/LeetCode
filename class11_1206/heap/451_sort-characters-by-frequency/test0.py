import collections
import heapq


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        # accept (None heap type)

        counter = collections.Counter(s)

        res = ''

        counter = counter.most_common()
        for value, count in counter:
            res += value * count

        return res


if __name__ == '__main__':
    object = Solution()
    s = "tree"
    print(object.frequencySort(s))
    object1 = Solution()
    s = "cccaaa"
    print(object1.frequencySort(s))
    object2 = Solution()
    s = "Aabb"
    print(object2.frequencySort(s))