from typing import List


class Solution:
    def rob(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return arr[0]

        def tabulation(nums: List[int]):
            n = len(nums)
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            for i in range(1, n):
                pick = nums[i]
                if i > 1:
                    pick += dp[i - 2]
                notpick = 0 + dp[i - 1]
                dp[i] = max(pick, notpick)
            return dp[n - 1]

        return max(tabulation(arr[1:]), tabulation(arr[:-1]))
