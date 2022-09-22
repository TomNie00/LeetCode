import math

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        digits = '0123456789'
        # s= s.strip()
        idx = 0
        sign = '+'
        while idx < len(s):
            if s[idx] in digits:
                num = 0
                num = num * 10 + int(s[idx])
                while idx + 1 < len(s) and s[idx + 1] in digits:
                    idx += 1
                    num = num * 10 + int(s[idx])
                idx += 1

                if sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                elif sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
            else:
                if s[idx] == '*':
                    sign = '*'
                    idx += 1
                elif s[idx] == '/':
                    sign = '/'
                    idx += 1
                elif s[idx] == '+':
                    sign = '+'
                    idx += 1
                elif s[idx] == '-':
                    sign = '-'
                    idx += 1
                else:
                    idx += 1
        return int(math.fsum(stack))




        # elements = []
        # stack = []
        # digits = '0123456789'
        # operators = '+-*/'
        # cur_int = 0
        # cur_num = 0
        # s = s.strip()
        # cur_num = 0
        #
        # #
        # idx = 0
        # while idx < len(s):
        #     if s[idx] in digits:
        #         cur_num = cur_num * 10 + int(s[idx])
        #         if s[idx] in operators and len(stack) == 0:
        #             stack.append(cur_num)
        #         idx += 1
        #     else:
        #         if s[idx] in operators:
        #             if s[idx] == '+':
        #                 stack.append(int(stack.pop()+cur_num))
        #                 idx += 1
        #             elif s[idx] == '-':
        #                 stack.append(int(stack.pop()-cur_num))
        #                 idx += 1
        #             elif s[idx] == '*':
        #                 stack.append(int(stack.pop() * cur_num))
        #                 idx += 1
        #             else:
        #                 stack.append(int(stack.pop() / cur_num))
        #                 idx += 1
        # return stack[0]








        #     e = elements[idx]
        #     if s(e) not in operators:
        #         stack.append(e)
        #         idx += 1
        #     else:
        #         # must be an operator
        #         if e in '*/':
        #             right_element = elements[idx + 1]
        #             left_element = stack.pop()
        #             if e == '*':
        #                 result = left_element * right_element
        #             else:
        #                 result = left_element // right_element
        #
        #             stack.append(result)
        #             idx += 2
        #         else:
        #             # must be + or -
        #             stack.append(e)
        #             idx += 1
        #
        # right_element = 0
        #
        # # 优化
        #
        # idx = 1
        # result = stack[0]
        # while idx < len(stack):
        #     if stack[idx] == '-':
        #         result -= stack[idx + 1]
        #         idx += 2
        #     else:
        #         result += stack[idx + 1]
        #         idx += 2
        #
        # return result


        # tooooooooo  Slow  in txt delete ""
        # result = 0
        # for c in stack:
        #
        #     result += c
        # while len(stack) > 1:
        #     cur_element = stack.pop(0)
        #     if s(cur_element) not in '+-':
        #         left_element = cur_element
        #     else:
        #         right_element = stack.pop(0)
        #         if cur_element == '+':
        #             result = left_element + right_element
        #         else:
        #             result = left_element - right_element
        #         stack.insert(0, result)
        #
        # return stack[0]




if __name__ == '__main__':
    # with open('large_input.txt') as f:
    #     lines = f.readlines()
    # large_input = lines[0]
    # s = large_input

    obj = Solution()
    s = "14-3/2"
    res = obj.calculate(s)

    print(res)
