from typing import List


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = 9
        ans = []

        def helper(ind: int, aim: int, temp: List[int]) -> None:
            if aim == 0 and len(temp) == k:
                ans.append(temp)
                return
            if ind == n:
                return
            helper(ind + 1, aim, temp)
            if arr[ind] <= aim:
                temp2 = temp.copy()
                temp2.append(arr[ind])
                helper(ind + 1, aim - arr[ind], temp2)

        helper(0, target, [])
        return ans
