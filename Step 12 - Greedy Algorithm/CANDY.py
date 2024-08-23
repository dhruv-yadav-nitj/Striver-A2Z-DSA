from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        count = [1 for _ in range(n)]
        # left neighbour
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                count[i] = count[i - 1] + 1
        # right neighbour
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                count[i] = max(count[i], count[i + 1] + 1)
        return sum(count)
