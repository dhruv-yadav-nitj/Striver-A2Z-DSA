from typing import List

'''
All the processes are available at t = 0.
'''


class Solution:
    def solve(self, bt: List[int]):
        time = ans = 0
        bt.sort()
        for i in bt:
            ans += time
            time += i
        print(time, ans)
        return ans // len(bt)
