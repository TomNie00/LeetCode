import math


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

        if self.heap_array[idx] < self.heap_array[parent]:
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
            if self.heap_array[right_idx] < self.heap_array[left_idx]:
                smaller_one = right_idx

        if self.heap_array[idx] > self.heap_array[smaller_one]:
            self.swap(idx, smaller_one)
            self._sift_down(smaller_one)

    def top(self):
        return self.heap_array[0]


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = int(math.pow(len(matrix), 2))
        res = 0
        myheap = Myheap(length)

        for i in matrix:
            for y in i:
                myheap.insert(y)

        while k:
            k -= 1
            res = myheap.pop()

        return res


if __name__ == '__main__':
    object = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8

    print(object.kthSmallest(matrix, k))

    object1 = Solution()
    matrix = [[-5]]
    k = 1
    print(object1.kthSmallest(matrix, k))
