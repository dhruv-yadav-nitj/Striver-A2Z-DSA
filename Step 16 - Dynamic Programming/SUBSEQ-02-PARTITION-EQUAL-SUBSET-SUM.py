from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1:
            return False
        else:
            target //= 2

            def tabulation():
                n = len(nums)
                dp = [[False for _ in range(target + 1)] for _ in range(n)]
                for i in range(n):
                    dp[i][0] = True
                if nums[0] <= target:
                    dp[0][nums[0]] = True
                for i in range(1, n):
                    for summ in range(1, target + 1):
                        notpick = dp[i - 1][summ]
                        pick = False
                        if nums[i] <= summ:
                            pick = dp[i - 1][summ - nums[i]]
                        dp[i][summ] = pick or notpick
                return dp[n - 1][target]

            return tabulation()
