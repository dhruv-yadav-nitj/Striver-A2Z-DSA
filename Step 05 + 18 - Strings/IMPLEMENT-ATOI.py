class Solution:
    def __init__(self):
        self.maxi = 2 ** 31 - 1
        self.mini = -(2 ** 31)

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        if len(s):
            if s[0] in ['+', '-']:
                if s[0] == '-':
                    sign = -1
                s = s[1:]
            ans = 0
            for item in s:
                if item.isdigit():
                    ans = ans * 10 + int(item)
                else:
                    break
            ans = ans * sign
            return max(self.mini, min(self.maxi, ans))
        else:
            return 0
