class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        symbolValue = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }

        ans = ''
        list1 = []
        i = 0
        if num == 0:
            return 0
        if num < 0:
            num = 2**32 + num
        while num > 0:
            n = num % 16
            num = num // 16
            if n < 10:
                ans += str(n)  # str() converts value to string
                # list1.append(str(n))
                # i += 1
            else:
                ans += symbolValue[n]
                # list1.append(symbolValue[n])  #better use [] instead of () when trying to use dict
                # i += 1

        # list1.reverse()
        # for i in range(len(list1)):
        #     ans += list1[i]

        return ans[:: -1]




if __name__ == "__main__":
    obj = Solution()

    num = -1

    answer = obj.toHex(num)

    print(answer)
