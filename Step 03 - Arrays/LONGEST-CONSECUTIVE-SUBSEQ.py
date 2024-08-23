from typing import List


class Solution:
    def findLongestConseqSubseq(self, arr: List[int], n: int):
        arr.sort()
        count = ans = 1
        n, last, curr = len(arr), 0, 1
        while curr < n:
            while curr < n and arr[curr] == arr[curr - 1]:
                curr += 1
                if curr >= n:
                    break
            if arr[curr] == arr[last] + 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
            last, curr = curr, curr + 1
        return ans
