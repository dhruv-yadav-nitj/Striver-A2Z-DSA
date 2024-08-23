class Solution:
    def setBit(self, n):
        mask = n ^ (n + 1)
        return n | mask
