class Solution:
    def generateBinaryStrings(self, n):
        ans = []

        def helper(ind: int, s: str, prev=False) -> None:
            if ind == n:
                ans.append(s)
                return
            helper(ind + 1, s + "0", False)
            if not prev:
                helper(ind + 1, s + "1", True)

        helper(0, "", False)
        return ans
