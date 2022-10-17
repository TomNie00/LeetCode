class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # submit accept

        res = []
        element = []

        def backtracking(start, element):
            if len(element) == k:
                # when the element length equals to k then add it into res
                res.append(element[:])
                return

            for i in range(start, n+1):
                # since we do not want the duplicate number so the start position should be the start passed in
                element.append(i)
                # add i
                backtracking(i + 1, element)
                # pass i + 1 as start so we can avoid duplicate number of combination
                element.pop()
                # pop the element that we add for future use

        backtracking(1,element)
        # the start position is always be the 1
        return res


if __name__ == '__main__':
    object = Solution()

    n = 4
    k = 2

    print(object.combine(n,k))
