from typing import List

# This problem was asked to me in my Info Edge Interview Round 1. But I was also asked to print all the denominations which
# are included in the answer!

# Standard Problem
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def tabulation():
            dpp = [[0 for _ in range(amount+1)] for _ in range(n)]
            for i in range(amount + 1):
                dpp[0][i] = i // coins[0] if i % coins[0] == 0 else int(1e9)
            for i in range(1, n):
                for amt in range(amount + 1):
                    not_take = dpp[i-1][amt]
                    take = int(1e9)
                    if coins[i] <= amt:
                        take = 1 + dpp[i][amt - coins[i]]
                    dpp[i][amt] = min(take, not_take)
            
            # Printing the denominatons which we are taking to make our amount!
            ans = []
            i = n - 1
            j = amount
            res = dpp[n-1][amount]
            if res < int(1e9):
                while i >= 0 and j > 0:
                    if i > 0 and dpp[i-1][j] == dpp[i][j]:
                        i -= 1
                    elif dpp[i][j - coins[i]] + 1 == dpp[i][j]:
                        ans.append(coins[i])
                        j -= coins[i]
                print(ans)
            return res
            

        def memo(i: int, rem: int) -> int:
            if rem == 0:
                return 0
            if i >= n:
                return int(1e9)
            if dp[i][rem] != -1:
                return dp[i][rem]
            op1 = op2 = int(1e9)
            if coins[i] <= rem:
                op1 = 1 + memo(i, rem - coins[i])
            op2 = 0 + memo(i+1, rem)
            dp[i][rem] = min(op1, op2)
            return dp[i][rem]
        ans = tabulation()
        return ans if ans < int(1e9) else -1

# Standard Problem with Tweaks -> Print All the Denominations That You Are Taking!

obj = Solution()
coins = list(map(int, input().split()))
amount = int(input())
print(obj.coinChange(coins, amount))