from typing import List
from collections import defaultdict
import heapq
from queue import Queue

'''
This problem has multiple implementations!
It can be done using 1: heapq and map or 2: only map.s
Time Complexity in both would be the same approx.!
'''


class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.time = 1
        self.timeline = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.timeline, (-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        q = Queue()
        while len(feed) < 10 and len(self.timeline):
            t, t_id, u_id = heapq.heappop(self.timeline)
            q.put((t, t_id, u_id))
            if u_id in self.following[userId] or u_id == userId:
                feed.append(t_id)
        while not q.empty():
            heapq.heappush(self.timeline, q.get())
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
