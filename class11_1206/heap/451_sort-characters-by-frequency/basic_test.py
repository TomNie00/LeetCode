import collections
import heapq

# from class11_1206.heap.Basic.Frequency.utils import Myheap

class Myheap(object):
    def __init__(self, size):
        self.heap_size = size
        self.heap_array = []

    def swap(self, idx1, idx2):
        self.heap_array[idx1], self.heap_array[idx2] = self.heap_array[idx2], self.heap_array[idx1]

    def insert(self, x):
        if len(self.heap_array) == self.heap_size:
            return False
        else:
            self.heap_array.append(x)
            self._sift_up(len(self.heap_array) - 1)

    def pop(self):
        self.swap(0, len(self.heap_array) - 1)
        pop_value = self.heap_array.pop()
        self._sift_down(0)

        return pop_value

    def _sift_up(self, idx):
        if idx == 0:
            return

        parent = (idx - 1) // 2

        if self.heap_array[idx][1] < self.heap_array[parent][1]:
            self.swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        if idx >= len(self.heap_array):
            return

        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2

        if left_idx >= len(self.heap_array):
            return

        smaller_one = left_idx

        if right_idx < len(self.heap_array):
            if self.heap_array[right_idx][1] < self.heap_array[left_idx][1]:
                smaller_one = right_idx

        if self.heap_array[idx][1] > self.heap_array[smaller_one][1]:
            self.swap(idx, smaller_one)
            self._sift_down(smaller_one)

    def top(self):
        return self.heap_array[0]


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = collections.Counter(s)
        myheap = Myheap(len(s))
        res = []

        for key, value in count.items():
            myheap.insert([key, value])

        while len(myheap.heap_array) > 0:
            v, k = myheap.pop()
            res.append(k * v)

        return ''.join(res)[::-1]



if __name__ == '__main__':
    object = Solution()
    s = "tree"
    print(object.frequencySort(s))

    object1 = Solution()
    s = "cccaaa"
    print(object1.frequencySort(s))

    object1 = Solution()
    s = "Aabb"
    print(object1.frequencySort(s))

