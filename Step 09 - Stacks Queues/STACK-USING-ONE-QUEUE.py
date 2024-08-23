from queue import Queue, PriorityQueue


class MyStack:

    def __init__(self):
        self.q = Queue()
        self.tp = -1

    def push(self, x: int) -> None:
        self.q.put(x)
        self.tp = x

    def pop(self) -> int:
        n = self.q.qsize()
        while n > 1:
            temp = self.q.get()
            self.q.put(temp)
            n -= 1
            self.tp = temp
        ans = self.q.get()
        if self.q.empty():
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
