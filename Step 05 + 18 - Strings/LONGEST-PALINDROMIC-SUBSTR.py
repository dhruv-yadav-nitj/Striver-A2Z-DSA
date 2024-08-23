class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def helper(l: int, r: int):
            nonlocal ans
            while l >= 0 and r < n and s[l] == s[r]:
                size = r - l + 1
                if size > len(ans):
                    ans = s[l:r + 1]
                l -= 1
                r += 1
            return ans

        for i in range(n):
            left = right = i
            ans = helper(left, right)
            left = i
            right = i + 1
            ans = helper(left, right)

        return ans
