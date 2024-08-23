from typing import List
from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-count for count in Counter(tasks).values()]
        print(tasks)
        heapq.heapify(tasks)
        time = 1
        q = deque()
        while len(tasks) or len(q):
            if len(tasks):
                count = heapq.heappop(tasks)
                count += 1
                if count:
                    q.append((time + n, count))
            if len(q):
                if time == q[0][0]:
                    heapq.heappush(tasks, q.popleft()[1])
            time += 1
        return time - 1
