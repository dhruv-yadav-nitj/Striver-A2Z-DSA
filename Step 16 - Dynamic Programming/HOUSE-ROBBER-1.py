from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1 for _ in range(n)]

        def memo(ind: int):
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            pick = nums[ind] + memo(ind + 2)
            notpick = 0 + memo(ind + 1)
            dp[ind] = max(pick, notpick)
            return dp[ind]

        def tabulation():
            dpp = [0 for _ in range(n)]
            dpp[0] = nums[0]
            for i in range(1, n):
                pick = nums[i]
                if i > 1:
                    pick += dpp[i - 2]
                notpick = 0 + dpp[i - 1]
                dpp[i] = max(pick, notpick)
            return dpp[n - 1]

        return tabulation()
