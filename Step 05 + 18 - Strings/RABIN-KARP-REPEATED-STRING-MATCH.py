# For BEST Explanation see -> Abdul Bari YouTube Video

# RABIN KARP ALGORITHM
class Solution:
    def RabinKarp(self, text: str, pattern: str) -> bool:
        n = len(text)
        m = len(pattern)
        if m > n:
            return False
        mod = 101
        base = 256
        p = t = 0
        h = pow(base, m - 1) % mod
        i = 0
        while i < m:
            p = (p * base + ord(pattern[i])) % mod
            t = (t * base + ord(text[i])) % mod
            i += 1
        i = 0
        while i <= n - m:
            if p == t:
                if text[i:i + m] == pattern:
                    return True
            j = i + m
            if j < n:
                t = (((t - ord(text[i]) * h) * base) + ord(text[j])) % mod
                if t < 0:
                    t = mod
            i += 1
        return False

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        max_attempt = m // n + 2
        s = ""
        # if not possible in max_attempts then it is certainly not possible!
        for attempt in range(max_attempt):
            s += a
            if self.RabinKarp(s, b):
                return attempt + 1
        return -1
