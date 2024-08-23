from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

        def tabulation():
            dpp = [1 for _ in range(n)]
            for curr in range(1, n):
                for prev in range(curr):
                    if nums[curr] > nums[prev]:
                        dpp[curr] = max(dpp[curr], dpp[prev] + 1)
            return max(dpp)

        def memo(i: int, prev: int):
            if i == n:
                return 0
            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]
            pick = 0
            if prev == -1 or nums[i] > nums[prev]:
                pick = 1 + memo(i + 1, i)
            not_pick = 0 + memo(i + 1, prev)
            dp[i][prev + 1] = max(pick, not_pick)
            return dp[i][prev + 1]

        return tabulation()
