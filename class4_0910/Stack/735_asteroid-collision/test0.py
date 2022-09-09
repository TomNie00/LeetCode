class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for char in asteroids:
            if char > 0:
                stack.append(char)
            else:
                while stack is not None and stack[-1] > 0 and stack[-1] < -char:
                    stack.pop()
                if stack is not None and stack[-1] > 0:
                    if stack[-1] == -char:
                        stack.pop()
                else:
                    stack.append(char)

        return stack


if __name__ == '__main__':
    s = [10,2,-5]
    obj = Solution()

    res = obj.asteroidCollision(s)
    print(res)