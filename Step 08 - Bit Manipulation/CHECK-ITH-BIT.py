class BruteForce:
    def checkKthBit(self, n: int, k: int) -> bool:
        binary = bin(n)[1:]
        return k < len(binary) and binary[-k - 1] == '1'


class Solution:
    def checkKthBit(self, n: int, k: int) -> bool:
        return (n >> k & 1)
