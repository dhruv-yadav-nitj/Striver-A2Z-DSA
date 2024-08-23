class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while len(self.stack) and self.stack[-1][0] <= price:
            cnt += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, cnt))
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
