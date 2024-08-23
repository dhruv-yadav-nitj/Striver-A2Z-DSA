from collections import defaultdict, Counter
from queue import PriorityQueue


# Approach 1
class Solution1:
    def frequencySort(self, s: str) -> str:
        # mp = defaultdict(int, {key: s.count(key) for key in set(s)})
        mp = defaultdict(int, Counter(s))
        pq = PriorityQueue()
        for key, value in mp.items():
            pq.put((-value, key))
        ans = ""
        while not pq.empty():
            k, v = pq.get()
            ans += v * (-k)
        return ans


# Approach 2
class Solution2:
    def frequencySort(self, s: str) -> str:
        mp = defaultdict(int, Counter(s))
        temp = [(k, v) for k, v in mp.items()]
        temp.sort(reverse=True, key=lambda x: x[1])
        ans = ""
        for c, f in temp:
            ans += str(c) * f
        return ans
