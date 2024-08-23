class Solution:
    @staticmethod
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        t = s[::-1]
        return s == t
