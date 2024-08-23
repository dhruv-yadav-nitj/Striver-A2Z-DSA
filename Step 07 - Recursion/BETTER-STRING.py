from typing import Dict


class Solution1:
    def betterString(self, str1: str, str2: str):
        set1 = set()
        set2 = set()

        def helper(ind: int, n: int, s: str, temp: str, st: set):
            if ind == n:
                st.add(temp)
                return
            helper(ind + 1, n, s, temp + s[ind], st)
            helper(ind + 1, n, s, temp, st)

        helper(0, len(str1), str1, "", set1)
        helper(0, len(str2), str2, "", set2)

        cnt1 = len(set1)
        cnt2 = len(set2)
        return str1 if cnt1 >= cnt2 else str2


class Solution:
    def betterString(self, s1: str, s2: str):
        set1 = {}
        set2 = {}

        def memo(ind: int, n: int, s: str, temp: str, st: Dict):
            if ind == n:
                return 1
            if (ind, temp) in st:
                return st[(ind, temp)]
            include = memo(ind + 1, n, s, temp + s[ind], st)
            exclude = memo(ind + 1, n, s, temp, st)
            st[(ind, temp)] = include + exclude
            return st[(ind, temp)]

        cnt1 = memo(0, len(s1), s1, "", set1)
        cnt2 = memo(0, len(s2), s2, "", set2)
        return s1 if cnt1 >= cnt2 else s2
