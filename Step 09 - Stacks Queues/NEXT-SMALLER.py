from typing import List


class Solution:
    def help_classmate(self, arr: List[int], n: int):
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and stack[-1] >= arr[i]:
                stack.pop()
            temp = arr[i]
            if len(stack):
                arr[i] = stack[-1]
            else:
                arr[i] = -1
            stack.append(temp)
        return arr
