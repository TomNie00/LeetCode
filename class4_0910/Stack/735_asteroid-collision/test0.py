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
                while len(stack) != 0:
                    if stack[-1] > 0 and stack[-1] < -char:
                        # 判断栈顶元素是否为正同时判断是否小于char的绝对值
                        stack.pop()
                    else:
                        break
                if len(stack) != 0:
                    if stack[-1] > 0:
                        if stack[-1] == -char:
                            # 判断是否两数是否相等
                            stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)

        return stack


if __name__ == '__main__':
    s = [-2,-1,1,2]
    obj = Solution()

    res = obj.asteroidCollision(s)
    print(res)
