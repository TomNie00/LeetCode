import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]] (u, v, w) = (node, target, cost)
        :type n: int (n nodes)
        :type k: int (start at k node)
        :rtype: int
        """

        record_time = [float("inf") for i in range(n + 1)]
        record_time[0] = 0
        print(record_time)

        graph_dict = collections.defaultdict(list)

        heap = [(0, k)]

        for node, target, cost in times:
            graph_dict[node].append((target, cost))

        while heap:
            time, node = heapq.heappop(heap)
            if time < record_time[node]:
                record_time[node] = time
                for target, cost in graph_dict[node]:
                    heapq.heappush(heap, (time + cost, target))

        min_time = max(record_time)
        return min_time if min_time != float('inf') else -1


if __name__ == '__main__':
    obj = Solution()

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    print(obj.networkDelayTime(times, n, k))