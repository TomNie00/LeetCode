class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        index = 0
        while index < len(s):
            cur_char = s[index]
            cur_value = char_map[cur_char]
            ans += cur_value
            index += 1
        return ans

if __name__ == "__main__":
    obj = Solution()

    s = "III"
    print(s)
    ans = obj.romanToInt(s)
    print(ans)
    print('\n---\n')

    s = "LVIII"
    print(s)
    ans = obj.romanToInt(s)
    print(ans)
    print('\n---\n')