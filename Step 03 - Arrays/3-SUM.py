from typing import List
from collections import defaultdict


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), set()
        for i in range(n):
            st = set()
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if target in st:
                    p, q, r = nums[i], nums[j], target
                    ans.add(sorted((p, q, r)))
                st.add(nums[j])
        return list(ans)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates
            j, k = i + 1, n - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif res > 0:
                    k -= 1
                else:
                    j += 1
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
        return ans
