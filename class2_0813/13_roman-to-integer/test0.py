class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbolValue = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        n = 0

        while n < len(s):
            if n == len(s) - 1:
                ans += symbolValue[s[n]]
                n += 1
            else:
                if symbolValue[s[n]] < symbolValue[s[n + 1]]:
                    ans += symbolValue[s[n + 1]] - symbolValue[s[n]]
                    n += 2
                else:
                    ans += symbolValue[s[n]]
                    n += 1

        return ans


if __name__ == "__main__":
    obj = Solution()

    # s = "LVIII"
    # s = "III"
    s = "MCMXCIV"
    print(s)
    ans = obj.romanToInt(s)
    print(ans)
    print('\n---\n')
