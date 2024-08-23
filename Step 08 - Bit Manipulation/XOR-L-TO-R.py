from functools import reduce


class BruteForce:
    def findXOR(self, l: int, r: int):
        arr = [i for i in range(l, r + 1)]
        return reduce(lambda x, y: x ^ y, arr)


class Solution:
    def helper(self, n: int):
        mod = n % 4
        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        else:
            return 0

    def findXOR(self, l: int, r: int):
        xor1 = self.helper(r)  # 1 ^ 2 ^ 3 ^ 4 ^ ...... ^ r
        xor2 = self.helper(l - 1)  # 1 ^ 2 ^ 3 ^ 4 ^ ... ^ l-1
        return xor1 ^ xor2
