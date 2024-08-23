from queue import Queue


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.tp = -1

    def push(self, x: int) -> None:
        self.q1.put(x)
        self.tp = x

    def pop(self) -> int:
        if self.tp == -1:
            return -1
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        ans = self.q1.get()
        if self.q2.qsize():
            while self.q2.qsize():
                temp = self.q2.get()
                self.q1.put(temp)
                self.tp = temp
        else:
            self.tp = -1
        return ans

    def top(self) -> int:
        return self.tp

    def empty(self) -> bool:
        return self.tp == -1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
