from typing import List
from queue import Queue


class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        mod = int(1e5)
        count = [int(1e9) for _ in range(mod)]  # max we can reach upto (mod - 1) bcz we have to take mod
        q = Queue()
        q.put((0, start))
        while not q.empty():
            cnt, curr = q.get()
            if curr == end:
                return cnt
            for i in arr:
                t = (curr * i) % mod
                if count[t] > cnt + 1:
                    count[t] = cnt + 1
                    q.put((count[t], t))
        return -1
