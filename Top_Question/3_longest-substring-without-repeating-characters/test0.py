class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # submit accept

        left = 0
        right = 0
        result = 0
        non_repeat_characters = set()
        
        while right < len(s):
            if s[right] not in non_repeat_characters:
                # if non repeating we add it to non repeating set
                non_repeat_characters.add(s[right])
                right += 1
                # index move forward
                result = max(result, len(non_repeat_characters))
                # get the bigger length of the non repeating
            else:
                non_repeat_characters.remove(s[left])
                # we have to keep remove left elements until s[right] is not in the non repeating set
                left += 1
                # move forward

        return result
                