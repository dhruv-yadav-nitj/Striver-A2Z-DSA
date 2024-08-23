from typing import List

"""
Solution would work only when 0 <= arr[i]
"""


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        dp = [[False for _ in range(total + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        # print(dp)
        dp[0][nums[0]] = True  # to handle the case when we have only one element
        for i in range(1, n):
            for j in range(total + 1):
                not_take = dp[i - 1][j]
                take = False
                if j >= nums[i]:
                    take = dp[i - 1][j - nums[i]]
                dp[i][j] = take or not_take
        for j in range(total // 2, -1, -1):
            if dp[n - 1][j]:
                return abs(j - (total - j))
        return -1
