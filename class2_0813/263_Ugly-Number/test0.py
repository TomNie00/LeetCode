class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n <= 0:
            return False
        else:
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                elif n % 3 == 0:
                    n = n / 3
                elif n % 5 == 0:
                    n = n / 5
                else:
                    return False
            return True


if __name__ == "__main__":
    obj = Solution()

    n = 6
    # n = 1
    # n =14
    result = obj.isUgly(n)
    print(result)
