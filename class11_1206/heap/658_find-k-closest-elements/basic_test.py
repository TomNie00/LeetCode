from class11_1206.heap.Basic.Frequency.utils import Myheap

# class Myheap(object):
#     def __init__(self, size):
#         self.heap_size = size
#         self.heap_array = []
#
#     def swap(self, idx1, idx2):
#         self.heap_array[idx1], self.heap_array[idx2] = self.heap_array[idx2], self.heap_array[idx1]
#
#     def insert(self, x):
#         if len(self.heap_array) == self.heap_size:
#             return False
#         else:
#             self.heap_array.append(x)
#             self._sift_up(len(self.heap_array) - 1)
#
#     def pop(self):
#         self.swap(0, len(self.heap_array) - 1)
#         pop_value = self.heap_array.pop()
#         self._sift_down(0)
#
#         return pop_value
#
#     def _sift_up(self, idx):
#         if idx == 0:
#             return
#
#         parent = (idx - 1) // 2
#
#         if self.heap_array[idx][1] < self.heap_array[parent][1]:
#             self.swap(idx, parent)
#             self._sift_up(parent)
#
#     def _sift_down(self, idx):
#         if idx >= len(self.heap_array):
#             return
#
#         left_idx = 2 * idx + 1
#         right_idx = 2 * idx + 2
#
#         if left_idx >= len(self.heap_array):
#             return
#
#         smaller_one = left_idx
#
#         if right_idx < len(self.heap_array):
#             if self.heap_array[right_idx][1] < self.heap_array[left_idx][1]:
#                 smaller_one = right_idx
#
#         if self.heap_array[idx][1] > self.heap_array[smaller_one][1]:
#             self.swap(idx, smaller_one)
#             self._sift_down(smaller_one)
#
#     def top(self):
#         return self.heap_array[0]

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        myheap = Myheap(len(arr))
        res = []

        for i in arr:
            distance = abs(i - x)
            myheap.insert([distance, i])

        while k > 0:
            k -= 1
            distance, i = myheap.pop()
            res.append(i)

        return sorted(res)


if __name__ == '__main__':
    object = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3

    print(object.findClosestElements(arr, k, x))

    object1 = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    print(object1.findClosestElements(arr,k,x))
