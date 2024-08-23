from typing import List


class Solution:
    def subsetSums(self, arr: List[int], n: int):
        arr.sort()
        ans = []

        def helper(ind: int, curr: int) -> None:
            if ind == n:
                ans.append(curr)
                return
            helper(ind + 1, curr)
            helper(ind + 1, curr + arr[ind])

        helper(0, 0)
        return ans
