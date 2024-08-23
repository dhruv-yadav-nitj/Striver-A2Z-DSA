from typing import List


class Solution:
    def count_NGEs(self, n: int, arr: List[int], queries: int, indices: List[int]) -> List[int]:
        ans = []
        for q in indices:
            cnt = 0
            for item in arr[q + 1:]:
                if item > arr[q]:
                    cnt += 1
            ans.append(cnt)
        return ans
