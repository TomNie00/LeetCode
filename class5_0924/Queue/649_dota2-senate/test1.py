from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        q_d = []
        q_r = []

        for idx, value in enumerate(senate):
            if value == "R":
                q_r.append(idx)
            else:
                q_d.append(idx)

        while len(q_d) != 0 and len(q_r) != 0:
            if q_d[0] < q_r[0]:
                q_r.pop(0)
                q_d.append(q_d.pop(0) + len(senate))
            else:
                q_d.pop(0)
                q_r.append(q_r.pop(0) + len(senate))

        if len(q_d) == 0:
            return "Radiant"
        return "Dire"
