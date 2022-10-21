class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # submit accept

        if n == 1:
            return "1"

        seq = self.countAndSay(n - 1)
        curr_number = seq[0]
        res = ""
        count = 1

        for i in range(1, len(seq)):
            if seq[i] == curr_number:
                count += 1
            else:
                res += str(count) + str(curr_number)
                curr_number = seq[i]
                count = 1

        res += str(count) + str(curr_number)

        return res

    #   res = "1"
    #   for i in range(n-1):
    #   res = self.next_seq(res)

    #   return res

    # def next_seq(self, res):
    #   i = 0
    #   new_seq = ''

    #   while i < len(res):
    #       count = 1
    #       while i < len(res) - 1 and res[i] == res[i+1]:
    #           count += 1
    #           i += 1
    #       new_seq += str(count) + str(res[i])
    #       i += 1
    #   return new_seq
