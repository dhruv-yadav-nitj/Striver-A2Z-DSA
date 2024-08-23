maxsize = 2 ** 31


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = maxsize

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val
        self.stack.append((val, self.minimum))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack):
            self.minimum = self.stack[-1][1]
        else:
            self.minimum = maxsize

    def top(self) -> int:
        if len(self.stack):
            a, b = self.stack[-1]
            return a
        else:
            return -1

    def getMin(self) -> int:
        return self.minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
