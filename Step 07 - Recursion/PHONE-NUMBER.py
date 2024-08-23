from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        n = len(digits)
        if n:
            ans = []

            def helper(ind: int, curr: str) -> None:
                if ind == n:
                    ans.append(curr)
                    return
                key = int(digits[ind])
                val = keypad[key]
                for i in range(len(val)):
                    helper(ind + 1, curr + val[i])

            helper(0, "")
            return ans
        else:
            return []
