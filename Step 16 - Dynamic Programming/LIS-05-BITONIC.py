from typing import List


class Solution:
    def LongestBitonicSequence(self, n: int, nums: List[int]) -> int:

        def helper(arr: List[int]):
            dp = [1 for _ in range(n)]
            for i in range(1, n):
                for j in range(i):
                    if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
            return dp

        lis1 = helper(nums)
        lis2 = list(reversed(helper(nums[::-1])))
        ans = 0
        for i in range(n):
            if lis1[i] > 1 and lis2[i] > 1:  # edge case: when we only have strictly inc or dec subsequence
                ans = max(ans, lis1[i] + lis2[i] - 1)
        return ans
