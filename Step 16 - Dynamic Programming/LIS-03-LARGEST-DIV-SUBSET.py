from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()  # we need to sort since the problem asks about Subset and not Subseq
        dp = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        index = 0
        maxi = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    prev[i] = j
                    dp[i] = dp[j] + 1
                    if maxi < dp[i]:
                        maxi = dp[i]
                        index = i
        ans = []
        while index != -1:
            ans.append(nums[index])
            index = prev[index]
        return list(reversed(ans))
