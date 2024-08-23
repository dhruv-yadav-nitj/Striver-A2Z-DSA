class Solution:
    def recursion(self, s: str, index: int, n: int, count: int) -> bool:
        # Base Condition
        if index >= n:
            return count == 0
        if count < 0:
            return False
        item = s[index]
        if item == '(':
            return self.recursion(s, index + 1, n, count + 1)
        elif item == ')':
            return self.recursion(s, index + 1, n, count - 1)
        else:
            op1 = self.recursion(s, index + 1, n, count + 1)
            op2 = self.recursion(s, index + 1, n, count)
            op3 = self.recursion(s, index + 1, n, count - 1)
            return op1 or op2 or op3

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def memo(index: int, count: int) -> bool:
            if index == n:
                return count == 0
            if count < 0:
                return False
            if dp[index][count] != -1:
                return dp[index][count]
            item = s[index]
            if item == '(':
                ans = memo(index + 1, count + 1)
            elif item == ')':
                ans = memo(index + 1, count - 1)
            else:
                op1 = memo(index + 1, count + 1)
                op2 = memo(index + 1, count - 1)
                op3 = memo(index + 1, count)
                ans = op1 or op2 or op3
            dp[index][count] = ans
            return ans
        return memo(0, 0)
