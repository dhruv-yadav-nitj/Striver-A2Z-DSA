class Solution:
    def InfixtoPostfix(self, exp: str):
        ans = ""
        n = len(exp)
        stack = []
        priority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        for i in range(n):
            c = exp[i]
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                # operand
                ans += c
            elif c == '(':
                # opening bracket
                stack.append(c)
            elif c == ')':
                # closing bracket
                while len(stack) and stack[-1] != '(':
                    ans += stack[-1]
                    stack.pop()
                if len(stack) and stack[-1] == '(':
                    stack.pop()
            else:
                # operator
                if len(stack):
                    while len(stack) and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
                        ans += stack[-1]
                        stack.pop()
                    stack.append(c)
                else:
                    stack.append(c)
        while len(stack):
            ans += stack[-1]
            stack.pop()
        return ans
