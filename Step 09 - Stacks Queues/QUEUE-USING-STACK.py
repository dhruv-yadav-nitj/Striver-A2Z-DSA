class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = -1

    def push(self, x: int) -> None:
        if not len(self.stack1):
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        ans = self.front
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        if len(self.stack1):
            self.stack1.pop()
        if len(self.stack2):
            self.front = self.stack2[-1]
        else:
            self.front = -1
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        return ans

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return self.front == -1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
