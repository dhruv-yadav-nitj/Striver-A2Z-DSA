from typing import List


# USING DYNAMIC PROGRAMMING
class Solution1:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def pussy(i, j, count):
            if count == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            op1 = cardPoints[i] + pussy(i + 1, j, count - 1)
            op2 = cardPoints[j] + pussy(i, j - 1, count - 1)
            dp[i][j] = max(op1, op2)
            return dp[i][j]

        return pussy(0, n - 1, k)


# USING SLIDING WINDOW
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        window = n - k
        curr = mini = sum(cardPoints[:window])
        for i in range(window, n):
            print(mini, curr)
            curr = curr + cardPoints[i] - cardPoints[i - window]
            mini = min(mini, curr)
        return sum(cardPoints) - mini
