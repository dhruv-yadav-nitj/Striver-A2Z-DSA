from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def isPalindrome(t: str) -> bool:
            m = len(t)
            if m <= 1:
                return True
            for i in range(m // 2):
                if t[i] != t[m - 1 - i]:
                    return False
            return True

        def helper(ind: int, text: str, curr: List[str]):
            if ind == n:  # base condition
                for item in curr:
                    if not isPalindrome(item):
                        return
                ans.append(curr)
                return

            for i in range(ind + 1, n + 1):
                temp = curr.copy()
                temp.append(text[ind:i])
                helper(i, text, temp)

        helper(0, s, [])
        return ans
