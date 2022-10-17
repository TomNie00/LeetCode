class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # submit accept

        res = []
        element = []
        count = {n: 0 for n in nums}
        # create a hashmap to reset the nums into a number + count type
        for n in nums:
            count[n] += 1
            # add the number of every number into the hashmap

        def dfs():
            if len(element) == len(nums):
                # when the element length equal to the nums length we append the element into our res
                res.append(element[:])
                # have to add [:] otherwise res will be empty
                return

            for num in count:
                # go over the numbers in the hashmap count to avoid duplicate
                if count[num] > 0:
                    # if the count of the number greater than 0 then we can add it into element
                    count[num] -= 1
                    # decrease the count by 1 since we add it
                    element.append(num)

                    dfs()
                    # call self to add the element into res

                    count[num] += 1
                    # after dfs() we have to reset the count for future use
                    element.pop()
                    # pop the element for future use

        dfs()
        return res


if __name__ == '__main__':
    object = Solution()

    nums = [1,1,2]

    print(object.permuteUnique(nums))