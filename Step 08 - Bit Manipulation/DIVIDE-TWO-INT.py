class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        d = abs(divisor)  # denominator
        n = abs(dividend)  # numerator
        ans = 0
        while n >= d:
            i = 0
            while n >= (d << i + 1):
                i += 1
            ans += (1 << i)
            n -= (d << i)
        ans = -ans if negative else ans
        return min(2 ** 31 - 1, max(-2 ** 31, ans))
