from typing import List
from queue import Queue


class Solution:
    def findOrder(self, dictionary: List[str], n: int, k: int) -> List[str]:
        def node(c: chr) -> int:
            return ord(c) - ord('a')

        adj = [[] for _ in range(k)]
        indegree = [0 for _ in range(k)]
        for i in range(1, n):
            item1 = dictionary[i - 1]
            item2 = dictionary[i]
            size = min(len(item1), len(item2))
            j = 0
            while j < size and item1[j] == item2[j]:
                j += 1
            if j < size:
                u = node(item1[j])
                v = node(item2[j])
                adj[u].append(v)
                indegree[v] += 1
        q = Queue()
        for i in range(k):
            if indegree[i] == 0:
                q.put(i)
        ans = []
        while not q.empty():
            curr = q.get()
            curr_char = chr(curr + ord('a'))
            ans.append(curr_char)
            for item in adj[curr]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    q.put(item)
        return ans
