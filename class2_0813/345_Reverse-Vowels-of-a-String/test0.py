class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = 'aeiou'
        str1 = ''
        i = 0
        j = len(s) - 1
        string = list(s)  # Can not modify the char of string, we have to convert the string to list
        while i < j:
            if string[i] not in vowels:
                i += 1
            elif string[j] not in vowels:
                j -= 1
            else:
                temp = string[i]
                string[i] = string[j]
                string[j] = temp
                i += 1
                j -= 1

        for x in range(len(string)):
            str1 += string[x]

        return str1


if __name__ == "__main__":
    object = Solution()

    # s = "hello"
    s = "leetcode"

    result = object.reverseVowels(s)
    print(result)
