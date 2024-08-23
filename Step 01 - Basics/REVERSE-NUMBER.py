class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        s = str(x)
        res, low, high = 0, -(2**31), (2**31)
        if s[0] == '-':
            s = s[1:]
            s = s[::-1]
            res = -1 * int(s)
        else:
            s = s[::-1]
            res = int(s)
        return 0 if res not in range(low, high) else res
