from typing import List

'''
Solution 1:
Traverse through each element and determing the prev_smaller_element and the next_smaller_element for this ith indexed
element -> to get the width for this rectangle -> (i - pse[i] + nse[i] - i - 1) = (nse[i] - pse[i] - 1) and height
would be obviously heights[i]
'''

'''
Solution 2:
Solution 1 could be optimised using stacks by storing the pse and nse for each element separately in different vectors.
But this solution is multi-pass solution and we need to traverse through the array 3 times to get the largest rectangle
area!
'''


class Optimised:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev_smaller = [-1 for _ in range(n)]
        stack = []
        for i, h in enumerate(heights):
            while len(stack) and heights[stack[-1]] >= h:
                stack.pop()
            if len(stack):
                prev_smaller[i] = stack[-1]
            stack.append(i)
        next_smaller = [n for _ in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack):
                next_smaller[i] = stack[-1]
            stack.append(i)

        return max([heights[i] * (i - prev_smaller[i] + next_smaller[i] - i - 1) for i in range(n)])


'''
Solution 3: Efficient : One-Pass Solution (Best Explanation Striver[New Video])
'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        ans = 0
        for i, h in enumerate(heights):
            while len(stack) and h < heights[stack[-1]]:
                nse = i
                curr = stack.pop()
                pse = -1
                if len(stack):
                    pse = stack[-1]
                ans = max(ans, (nse - pse - 1) * heights[curr])
            stack.append(i)
        while len(stack):
            nse = n
            curr = stack.pop()
            pse = -1
            if len(stack):
                pse = stack[-1]
            ans = max(ans, (nse - pse - 1) * heights[curr])
        return ans
