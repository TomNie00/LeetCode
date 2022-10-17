class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # submit accept

        # we have to break down into two sub-question
        # the first one is we have to find the greatest number in the nums1 and nums2
        # the second is we need to combine these two greatest number that we find
        #
        # since we only need k digits
        # we have serval situation:
        #
        # when k is >= nums1 and nums2:
        # first choose k digits from nums1 or nums2
        # second choose i digits from nums1 (nums2) and k - i digits from nums2 (nums1)
        # third
        #
        # when k is < nums1 or nums2: (we have to keep not out of range )
        # choose i digits (maybe i is the whole length of the num)
        # from nums1 (nums2) and k - i digits from nums2 (nums1)

        # use for i in range(k + 1) to try all the i and make sure not out of range

        def maxNumber(num, length):
            # find the the required length max number
            max_num = []
            num_pop = len(num) - length
            # this is how many times we can pop element

            for i in range(len(num)):
                while num_pop > 0 and len(max_num) and num[i] > max_num[-1]:
                    # we have to check we still have chance to pop and not pop from a empty max_num
                    # and if the number is greater than the top of max_num we pop and push num[i]
                    max_num.pop()
                    num_pop -= 1
                    # decrease the pop times
                max_num.append(num[i])

            return max_num[:length]
            # make sure we did not return more

        def merge_number(n1, n2):
            # merge two max_num to make it the biggest
            max_merge = []
            while n1 or n2:
                if n1 > n2:
                    # if n1 > n2 then we only need the first element of n1
                    max_merge.append(n1[0])
                    n1 = n1[1:]
                    # delete the first element
                else:
                    max_merge.append(n2[0])
                    n2 = n2[1:]

            return max_merge

        res = []

        for i in range(k + 1):
            # we try all the possible i
            if i > len(nums1) or k - i > len(nums2):
                # make sure we do not out of the range index
                continue
            ln1 = maxNumber(nums1, i)
            ln2 = maxNumber(nums2, k - i)

            res = max(res, merge_number(ln1, ln2))
            # compare itself with our new result to pick the greater one

        return res


if __name__ == '__main__':
    object = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5

    print(object.maxNumber(nums1, nums2, k))
