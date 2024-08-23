from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(ind: int, a: int, b: int, s: str) -> None:
            if ind == n:
                ans.append(s)
                return
            if a < n:
                helper(ind + 1, a + 1, b, s + '(')
            if a > 0 and b < a:
                helper(ind + 1, a, b + 1, s + ')')

        helper(0, 0, 0, "")
        return ans
