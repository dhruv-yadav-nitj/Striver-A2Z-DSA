from typing import Optional, List


class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


'''
1 <= deadline <= N 
'''
'''The strategy to maximize profit should be to pick up jobs that offer higher profits. Hence we should sort the jobs 
in descending order of profit. Now say if a job has a deadline of 4 we can perform it anytime between day 1-4, 
but it is preferable to perform the job on its last day. This leaves enough empty slots on the previous days to 
perform other jobs.'''


class Solution:
    def JobScheduling(self, jobs: List[Optional[Job]], n: int):
        jobs.sort(key=lambda x: -x.profit)
        booked = [False for _ in range(n + 1)]
        count = profit = 0
        for item in jobs:
            _, dead, prof = item.id, item.deadline, item.profit
            if not booked[dead]:
                booked[dead] = True
                count += 1
                profit += prof
            else:
                while dead and booked[dead]:
                    dead -= 1
                if dead >= 1:
                    booked[dead] = True
                    profit += prof
                    count += 1
        return count, profit
