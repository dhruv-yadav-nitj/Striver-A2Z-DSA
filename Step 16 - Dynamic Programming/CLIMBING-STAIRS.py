class Solution:
    def recursion(self, ind: int, n: int):
        if ind > n:
            return 0
        if ind == n:
            return 1
        choice1 = self.recursion(ind + 1, n)
        choice2 = self.recursion(ind + 2, n)
        return choice1 + choice2

    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n)]

        def memo(ind: int):
            if ind > n:
                return 0
            if ind == n:
                return 1
            if dp[ind] != -1:
                return dp[ind]

            choice1 = memo(ind + 1)
            choice2 = memo(ind + 2)
            dp[ind] = choice1 + choice2
            return dp[ind]

        def tabulation():
            dpp = [0 for _ in range(n + 1)]
            dpp[0] = dpp[1] = 1
            for i in range(2, n + 1):
                dpp[i] = dpp[i - 1] + dpp[i - 2]
            return dpp[n]

        return tabulation()
