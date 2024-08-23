from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs)
        i = 0
        while i < min(len(strs[0]), len(strs[n - 1])) and strs[0][i] == strs[n - 1][i]:
            i += 1
        return strs[0][:i]
