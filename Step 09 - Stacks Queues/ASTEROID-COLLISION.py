from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            if len(stack):
                if item > 0:
                    stack.append(item)
                else:
                    if stack[-1] < 0:
                        stack.append(item)
                    else:
                        while len(stack) and 0 < stack[-1] < abs(item):
                            stack.pop()
                        if len(stack):
                            if stack[-1] < 0:
                                stack.append(item)
                            else:
                                if stack[-1] == abs(item):
                                    stack.pop()
                                else:
                                    continue
                        else:
                            stack.append(item)
            else:
                stack.append(item)
        return stack
