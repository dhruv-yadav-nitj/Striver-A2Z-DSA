class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        kmp = KMP()
        return kmp.search(text, pattern)


class KMP:
    def __init__(self):
        pass

    def lps(self, target: str):
        m = len(target)
        lps = [0] * m
        i = 1
        j = 0
        while i < m:
            if target[i] == target[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return lps

    def search(self, text: str, pattern: str):
        n = len(text)
        m = len(pattern)
        i = j = 0
        lps = self.lps(pattern)
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:
                return i - j

            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
