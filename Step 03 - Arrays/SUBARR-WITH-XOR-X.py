from typing import List
from collections import defaultdict as hashmap


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A: List[int], B: int):
        xor, n, ans = 0, len(A), 0
        mp = hashmap(int)
        for i in range(n):
            xor ^= A[i]
            if xor == B:
                ans += 1
            target = xor ^ B
            ans += mp[target]
            mp[xor] += 1
        return ans
