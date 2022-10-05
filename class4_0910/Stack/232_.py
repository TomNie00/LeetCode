class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self,x):
        return self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def empty(self):
       return len(self.stack) == 0

class MyQueue(object):

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        s1, _ = self.get_main_stack()
        s1.push(x)


    def pop(self):
        """
        :rtype: int
        """
        s1, s2= self.get_main_stack()
        # after this no need to use self.s1 or self.s2 just go as s1 or s2
        last_ele = None

        while not s1.empty():
            cur = s1.pop()
            if s1.empty():
                last_ele = cur
            else:
                s2.push(cur)

        while not s2.empty():
            cur = s2.pop()
            s1.push(cur)

        return last_ele


    def peek(self):
        """
        :rtype: int
        """
        s1, s2 = self.get_main_stack()
        cur = None

        while not s1.empty():
            cur = s1.pop()
            s2.push(cur)

        while not s2.empty():
            s1.push(s2.pop())

        return cur


    def empty(self):
        """
        :rtype: bool
        """

        return self.s1.empty() and self.s2.empty()

    def get_main_stack(self):
        if self.s1.empty():
            return self.s2, self.s1
        return self.s1, self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
