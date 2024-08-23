class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = ""
        for c in s:
            if c == "(":
                if cnt:
                    ans += c
                else:
                    ans += ""
                cnt += 1
            else:
                if cnt > 1:
                    ans += c
                else:
                    ans += ""
                cnt -= 1
        return ans
