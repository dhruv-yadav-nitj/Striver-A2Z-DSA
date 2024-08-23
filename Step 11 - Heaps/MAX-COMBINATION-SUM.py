from typing import List
from queue import PriorityQueue


class Solution:
    def maxCombinations(self, n: int, k: int, a: List[int], b: List[int]):
        a.sort()
        b.sort()
        st = set()
        pq = PriorityQueue()
        pq.put((-(a[n - 1] + b[n - 1]), n - 1, n - 1))
        st.add((n - 1, n - 1))
        ans = []
        while not pq.empty() and len(ans) < k:
            curr, ci, cj = pq.get()
            ans.append(-curr)
            if len(ans) == k:
                return ans
            ti, tj = ci - 1, cj - 1
            if ti >= 0 and (ti, cj) not in st:
                pq.put((-(a[ti] + b[cj]), ti, cj))
                st.add((ti, cj))
            if tj >= 0 and (ci, tj) not in st:
                pq.put((-(a[ci] + b[tj]), ci, tj))
                st.add((ci, tj))

        return [-1] if not (len(ans)) else ans
