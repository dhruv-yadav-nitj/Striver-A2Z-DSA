class Solution:
    """
    Step 1: Reverse
    Step 2: Replace
    Step 3: Infix-Postfix (with one slight change in equality sign)
    Step 4: Reverse
    """
    def InfixtoPrefix(self, exp: str):
        exp = exp[::-1]
        s = ""
        for i in range(len(exp)):
            if exp[i] == '(':
                s += ')'
            elif exp[i] == ')':
                s += '('
            else:
                s += exp[i]
        ans = self.InfixtoPostfix(s)
        return ans[::-1]

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
                    while len(stack) and stack[-1] != '(' and priority[stack[-1]] > priority[c]:  # CHANGES
                        ans += stack[-1]
                        stack.pop()
                    stack.append(c)
                else:
                    stack.append(c)
        while len(stack):
            ans += stack[-1]
            stack.pop()
        return ans
