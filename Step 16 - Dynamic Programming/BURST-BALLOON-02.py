from typing import List

# https://leetcode.com/problems/burst-balloons/description/
# [MCM DP]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[-1 for _ in range(n+2)] for _ in range(n+2)]

        def solver(i: int, j: int) -> int:
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            maxi = 0
            for index in range(i, j+1):
                curr = nums[i-1] * nums[index] * nums[j+1] + \
                    solver(i, index-1) + solver(index+1, j)
                maxi = max(maxi, curr)
            dp[i][j] = maxi
            return maxi
        return solver(1, n)


def main():
    obj = Solution()
    nums = list(map(int, input().split()))
    print(obj.maxCoins(nums))


if __name__ == '__main__':
    main()


# VERDICT : AC