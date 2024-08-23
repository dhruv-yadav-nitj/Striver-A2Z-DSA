from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, arr: List[int]):
        xor = reduce(lambda x, y: x ^ y, arr)
        rightmost = (xor & xor - 1) ^ xor
        num1 = num2 = 0
        for item in arr:
            if item & rightmost:
                num1 = num1 ^ item
            else:
                num2 = num2 ^ item
        return [num1, num2]
