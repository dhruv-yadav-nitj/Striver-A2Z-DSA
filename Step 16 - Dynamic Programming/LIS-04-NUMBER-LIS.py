from typing import List


class Solution:
    def findNumberOfLIS(self, arr: List[int]):
        n = len(arr)
        dp = [1 for _ in range(n)]
        count = [1 for _ in range(n)]
        for i in range(1, n):
            maxi = 0
            for j in range(i):
                if arr[i] > arr[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        maxi = max(maxi, dp[i])
                        count[i] = count[j]
                    elif maxi == dp[j] + 1:
                        count[i] += count[j]
        # array contains duplicate elements!
        maxxi = max(dp)
        print(dp, count)
        ans = 0
        for i in range(n):
            if dp[i] == maxxi:
                ans += count[i]
        return ans
