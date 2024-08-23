class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return "0"
        if k == 0:
            return num
        num = list(map(int, num))
        stack = []
        i = 0
        while k and i < n:
            while k and len(stack) and stack[-1] > num[i]:
                k -= 1
                stack.pop()
            stack.append(num[i])
            i += 1
        if i < n:
            stack += num[i:]
        if k > 0:
            stack = stack[:-k]
        s = "".join(list(map(str, stack)))
        s = s.lstrip('0')
        return s if len(s) else "0"
