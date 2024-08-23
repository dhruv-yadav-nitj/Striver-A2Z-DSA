from typing import List


class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        total = sum(arr)
        if total < d:  # not possible if partition_sum is greater than total sum of array
            return 0
        subs1 = total - d
        if subs1 & 1:
            return 0
        else:
            target = subs1 // 2  # s1 = (total + d)//2 and s2 = (total - d)//2
            dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

            def memo(ind: int, rem: int) -> int:
                if ind == n - 1:
                    if rem == 0 and arr[ind] == 0:
                        return 2
                    elif rem == 0 or arr[ind] == rem:
                        return 1
                    else:
                        return 0
                if dp[ind][rem] != -1:
                    return dp[ind][rem]
                not_pick = memo(ind + 1, rem)
                pick = 0
                if arr[ind] <= rem:
                    pick = memo(ind + 1, rem - arr[ind])
                dp[ind][rem] = pick + not_pick
                return dp[ind][rem]

            return memo(0, target) % int(1e9 + 7)
