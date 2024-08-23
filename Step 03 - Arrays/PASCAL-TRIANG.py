from typing import List
from math import comb as ncr


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            curr = [-1 for _ in range(i+1)]
            for j in range(i//2 + 1):
                curr[j] = curr[i-j] = ncr(i, j)
            ans.append(curr)
        return ans
