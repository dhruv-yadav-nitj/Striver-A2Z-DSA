from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(2001)] for _ in range(n)]
        # 2001 bcz we need to have target + sum(arr) + 1 columns in dp to accomodate all the possible sums
        #/ and its upper limit acc to ques is 2000

        def memo(ind: int, rem: int):
            if ind == n:
                return 1 if rem == 0 else 0
            if dp[ind][rem] != -1:
                return dp[ind][rem]
            plus = memo(ind + 1, rem - nums[ind])
            mins = memo(ind + 1, rem + nums[ind])
            dp[ind][rem] = plus + mins
            return dp[ind][rem]

        return memo(0, target)
