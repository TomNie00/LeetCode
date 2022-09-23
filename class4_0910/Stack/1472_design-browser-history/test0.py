class BrowserHistory(object):
    # Passed
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.stack = []
        self.stack.append(homepage)
        self.pos = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        position = self.pos + 1
        self.stack[position:] = []
        self.stack.append(url)
        self.pos += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps < self.pos:
            self.pos -= steps
            return self.stack[self.pos]
        else:
            self.pos = 0
            return self.stack[self.pos]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps + self.pos >= len(self.stack):
            position = len(self.stack) - self.pos - 1
            self.pos += position
            return self.stack[self.pos]
        else:
            self.pos += steps
            return self.stack[self.pos]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)