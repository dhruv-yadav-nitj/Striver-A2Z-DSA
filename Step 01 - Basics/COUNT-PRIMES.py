class Solution:
    def isPrime(self, n):
        """
        SIEVE OF ERATOSTHENES
        """
        arr = [True for _ in range(n)]
        p = 2
        while p * p <= n:
            if arr[p]:
                for i in range(p * p, n, p):
                    arr[i] = False
            p += 1
        return arr

    def countPrimes(self, n: int) -> int:
        arr = self.isPrime(n)
        count = sum(1 for i in arr[2:] if i)
        return count
