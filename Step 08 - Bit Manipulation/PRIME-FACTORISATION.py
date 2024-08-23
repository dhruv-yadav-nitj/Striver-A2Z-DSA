from typing import List


class Solution:
    def sieve(self, n: int) -> List[int]:
        isPrime = [True for _ in range(n + 1)]
        for i in range(2, n + 1):
            if isPrime[i]:
                for p in range(i * i, n + 1, i):
                    isPrime[p] = False
        return isPrime

    def findPrimeFactors(self, n: int) -> List[int]:
        isPrime = self.sieve(n)
        ans = []
        for i in range(2, n + 1):
            if isPrime[i]:
                while n % i == 0:
                    ans.append(i)
                    n /= i
        return ans
