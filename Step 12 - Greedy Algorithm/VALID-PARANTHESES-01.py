class Solution1:
    def isValid(self, s: str) -> bool:
        count = 0
        for item in s:
            if item == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif item == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif item == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif item == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
