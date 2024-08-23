import sys

sys.set_int_max_str_digits(0)  # removing the limit on str to int conversion


class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = int(num)
        while num and not (num % 2):
            num = num // 10
        return str(num) if num > 0 else ""
