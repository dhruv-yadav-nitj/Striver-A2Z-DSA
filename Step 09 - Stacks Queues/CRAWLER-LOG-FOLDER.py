from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        op1, op2 = '../', './'
        for log in logs:
            if log == op1:
                if len(stack) > 0:
                    stack.pop(-1)
                else:
                    continue
            elif log == op2:
                continue
            else:
                log = log[:-1]
                stack.append(log)
        return len(stack)
