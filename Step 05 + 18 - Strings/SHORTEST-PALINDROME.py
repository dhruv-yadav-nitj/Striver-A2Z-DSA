class BruteForce:
    def checkPalindrome(self, s: str) -> bool:
        i = 0
        n = len(s)
        while i < n // 2:
            if s[i] != s[n - 1 - i]:
                return False
            i += 1
        return True

    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        rev = s[::-1]
        while i < n:
            temp = rev[:i] + s[:]
            if self.checkPalindrome(temp):
                return temp
            i += 1
        return rev + s


# Python internally uses KMP Algorithm!
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]
        n = len(s)
        for i in range(n):
            if s.startswith(t[i:]):
                return t[:i] + s
        return t + s
