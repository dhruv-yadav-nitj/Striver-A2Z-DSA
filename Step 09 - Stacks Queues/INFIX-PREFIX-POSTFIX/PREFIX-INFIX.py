class Solution:
    def preToInfix(self, exp: str):
        stack = []
        for item in exp[::-1]:
            if item.isalnum():
                stack.append(item)
            else:
                a = stack.pop()
                b = stack.pop()
                temp = f"({a}{item}{b})"
                stack.append(temp)
        return stack[-1]
