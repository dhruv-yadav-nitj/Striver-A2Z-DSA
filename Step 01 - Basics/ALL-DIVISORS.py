class Solution:
    def sumOfDivisors(self, N):
        """
        hint: calculate how many times the number 'i' fits into N
        """
        ans = 0
        for i in range(1, N+1):
            k = N // i
            ans += (i * k)
        return ans
