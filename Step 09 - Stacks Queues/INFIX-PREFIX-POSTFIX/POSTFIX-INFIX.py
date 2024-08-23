class Solution:
    def postToInfix(self, exp: str):
        n = len(exp)
        stack = []
        for i in range(n):
            c = exp[i]
            '''
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
            we have a function for this in python! isalnum()
            '''
            if c.isalnum():
                stack.append(c)
            else:
                a = stack.pop()
                b = stack.pop()
                temp = f"({b}{c}{a})"
                stack.append(temp)
        return stack[-1]
