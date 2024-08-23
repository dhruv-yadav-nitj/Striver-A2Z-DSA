class Solution:
    def postToPre(self, exp: str):
        stack = []
        for item in exp:
            if item.isalnum():
                stack.append(item)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                temp = item + top2 + top1
                stack.append(temp)
        return stack[-1]
