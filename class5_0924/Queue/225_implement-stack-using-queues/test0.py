from collections import deque


# deque could add or pop from left and right
class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0


class MyStack(object):

    def __init__(self):
        self.q1 = MyQueue()
        # when the __words__ this means the initial value of it.
        self.q2 = MyQueue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q1, _ = self._get_1st_2nd_q()
        # only care the first value.
        # no matter q1 or q2, we assign not empty one is q1
        # also can rewrite as _, q1
        # only care about the second value
        q1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        q1, q2 = self._get_1st_2nd_q()
        last_elem = None

        while not q1.empty():
            cur = q1.pop()
            if q1.empty():
                last_elem = cur
            else:
                q2.push(cur)

        return last_elem


    def top(self):
        """
        :rtype: int
        """
        q1, q2 = self._get_1st_2nd_q()
        cur = None

        while not q1.empty():
            cur = q1.pop()
            q2.push(cur)
        return cur




    def empty(self):
        """
        :rtype: bool
        """

        return self.q1.empty() and self.q2.empty()

    def _get_1st_2nd_q(self):
        if self.q1.empty():
            return self.q2, self.q1

        return self.q1, self.q2



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
