from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(arr: List[int], ind: int, n: int, temp: List[int], aim: int):
            if aim == 0:
                print(temp)
                ans.append(temp)
                return

            for i in range(ind, n):
                if i > ind and arr[i] == arr[i - 1]:
                    continue
                if arr[i] <= aim:
                    temp2 = temp.copy()
                    temp2.append(arr[i])
                    helper(arr, i + 1, n, temp2, aim - arr[i])
                else:
                    break
            return

        helper(candidates, 0, len(candidates), [], target)
        return ans
