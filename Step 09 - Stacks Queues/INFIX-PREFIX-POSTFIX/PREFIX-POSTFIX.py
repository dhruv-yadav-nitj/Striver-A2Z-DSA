class Solution:
    def preToPost(self, exp: str):
        stack = []
        for item in exp[::-1]:
            if item.isalnum():
                stack.append(item)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                temp = top1 + top2 + item
                stack.append(temp)
        return stack[-1]
