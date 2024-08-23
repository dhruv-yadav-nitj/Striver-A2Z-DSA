# USING SC: O(N)
class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)


# MOST OPTIMISED
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        cnt1 = cnt2 = 0
        for item in s:
            if item == '(':
                cnt1 += 1
            else:
                if cnt1 > 0:
                    cnt1 -= 1
                else:
                    cnt2 += 1
        return cnt1 + cnt2
