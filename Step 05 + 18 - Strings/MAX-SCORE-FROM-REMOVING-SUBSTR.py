class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x >= y:
            while True:
                arr = s.split("ab")
                if len(arr) > 1:
                    t = "".join(arr)
                    n = len(s) - len(t)
                    ans += (n // 2) * x
                    s = t
                else:
                    break
            while True:
                arr = s.split("ba")
                if len(arr) > 1:
                    t = "".join(arr)
                    n = len(s) - len(t)
                    ans += (n // 2) * y
                    s = t
                else:
                    break
        else:
            while True:
                arr = s.split("ba")
                if len(arr) > 1:
                    t = "".join(arr)
                    n = len(s) - len(t)
                    ans += (n // 2) * y
                    s = t
                else:
                    break
            while True:
                arr = s.split("ab")
                if len(arr) > 1:
                    t = "".join(arr)
                    n = len(s) - len(t)
                    ans += (n // 2) * x
                    s = t
                else:
                    break
        return ans
