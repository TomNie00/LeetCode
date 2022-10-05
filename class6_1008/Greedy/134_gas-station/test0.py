class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # submit accept

        tank = 0
        count = 0
        gas_cost = 0

        if sum(gas) < sum(cost):
            # if gas is smaller than the cost then no way to arrival
            return -1

        for i in range(len(gas)):
            # must be a way could arrival
            gas_cost = gas[i] - cost[i]
            tank += gas_cost

            if tank < 0:
                # if tank is negative then this point could not be the start point
                tank = 0
                count = i + 1

        return count


if __name__ == "__main__":
    obj = Solution()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    res = obj.canCompleteCircuit(gas, cost)

    print(res)
