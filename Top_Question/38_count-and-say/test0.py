class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # submit accept

        # # RECURSIVE
        # if n == 1:
        #     return "1"
        # seq = self.countAndSay(n - 1)
        # number = seq[0]
        # answer = ""
        # count = 1
        # for i in range(1, len(seq)):
        #     if seq[i] == number:
        #         count += 1
        #     else:
        #         answer += str(count) + str(number)
        #         count = 1
        #         number = seq[i]
        # answer += str(count) + str(number)
        # return answer


        # ITERATIVE
        seq = "1"
        for i in range(n - 1):
            seq = self.next_seq(seq)
        return seq

    def next_seq(self, res):
        i = 0
        next_seq = ''
        while i < len(res):
            count = 1
            while i < len(res) - 1 and res[i] == res[i + 1]:
                count += 1
                i += 1
            next_seq += str(count) + str(res[i])
            i += 1
        return next_seq
