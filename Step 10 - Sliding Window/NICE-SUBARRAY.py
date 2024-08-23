from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: x % 2, nums))
        n = len(nums)

        def helper(target):
            ans = temp = i = j = 0
            while j < n:
                temp += nums[j]
                while temp > target:
                    temp -= nums[i]
                    i += 1
                ans += (j - i + 1)
                j += 1
            return ans

        return helper(k) - helper(k - 1)
