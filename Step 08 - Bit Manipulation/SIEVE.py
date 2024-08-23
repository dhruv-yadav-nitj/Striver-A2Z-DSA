class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [True for _ in range(n+1)]
        for i in range(2, n+1):
            if isPrime[i]:
                for k in range(i*i, n+1, i):
                    isPrime[k] = False
        return isPrime[2:n].count(True)
