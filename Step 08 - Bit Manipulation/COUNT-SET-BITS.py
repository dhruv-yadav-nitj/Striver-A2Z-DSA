class Solution:
    def countSetBits(self, n):
        return bin(n).count('1')
