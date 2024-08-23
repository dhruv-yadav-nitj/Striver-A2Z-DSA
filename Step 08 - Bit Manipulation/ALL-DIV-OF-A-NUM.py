from math import sqrt


class Solution:
    def print_divisors(self, n: int):
        ans = []
        for i in range(1, int(sqrt(n)+1)):
            if not (n % i):
                ans.append(i)
                if i != n // i:
                    ans.append(n // i)
        return sorted(ans)
