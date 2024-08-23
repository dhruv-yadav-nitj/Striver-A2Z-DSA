from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()

        def helper(arr: List[int], ind: int, n: int, temp: List[int], aim: int):
            if ind == n:
                if not aim:
                    ans.add(tuple(temp))
                return
            if arr[ind] <= aim:
                temp2 = temp[:]
                temp2.append(arr[ind])
                helper(arr, ind, n, temp2, aim - arr[ind])
            helper(arr, ind + 1, n, temp, aim)
            return

        helper(candidates, 0, len(candidates), [], target)
        return list(map(lambda x: list(x), ans))
