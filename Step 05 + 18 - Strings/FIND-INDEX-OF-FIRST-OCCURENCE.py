class Solution1:
    def strStr(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if m > n:
            return -1
        for i in range(n):
            if s[i] == t[0]:
                if i + m > n:
                    continue
                else:
                    temp = s[i:i + m]
                    if temp == t:
                        return i
        return -1


# Just Python being Python!
class Solution2:
    def strStr(self, s, t):
        return s.find(t)
