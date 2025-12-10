import heapq
from collections import defaultdict

class Twitter:
    
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1  # increasing timestamp

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.followers[userId] | {userId}
        heap = []
        for u in users:
            for t in self.tweets[u][-10:]:
                # Push negative time to simulate max-heap
                heapq.heappush(heap, (-t[0], t[1]))
        res = []
        for _ in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
