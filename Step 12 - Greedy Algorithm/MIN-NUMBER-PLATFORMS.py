from typing import List


class Solution:
    def minimumPlatform(self, n: int, arr: List[int], dep: List[int]):
        n, nums = len(arr), []
        nums += [(i, 'a') for i in arr]
        nums += [(i, 'd') for i in dep]
        nums.sort()
        ans = count = 0
        for _, item in nums:
            if item == 'a':
                count += 1
            else:
                count -= 1
            ans = max(ans, count)
        return ans
