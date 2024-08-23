from typing import List


class Solution:
    def insert_at_bottom(self, stack: List[int], item: int):
        if not len(stack):
            stack.append(item)
        else:
            a = stack.pop()
            self.insert_at_bottom(stack, item)
            stack.append(a)

    def helper(self, stack: List[int]):
        if not len(stack):
            return
        a = stack.pop()
        self.helper(stack)
        self.insert_at_bottom(stack, a)

    def reverse(self, stack: List[int]):
        self.helper(stack)
        return stack
