from collections import deque, defaultdict
from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.user_feeds = defaultdict(deque)
        self.user_followers = defaultdict(set)
        self.curr_ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_feeds[userId].appendleft((self.curr_ts, tweetId))
        self.curr_ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        max_heap = []

        # Add first tweet of each feed to a max_heap
        feed = self.user_feeds[userId]
        if len(feed) > 0:
            heappush(max_heap, (-feed[0][0], feed[0][1], userId, 0))

        for follower in self.user_followers[userId]:
            feed = self.user_feeds[follower]
            if len(feed) > 0:
                heappush(max_heap, (-feed[0][0], feed[0][1], follower, 0))

        while len(max_heap) > 0:
            ts, tweetId, userId, idx = heappop(max_heap)
            tweets.append(tweetId)

            feed = self.user_feeds[userId]
            idx += 1
            if idx < len(feed):
                heappush(max_heap, (-feed[idx][0], feed[idx][1], userId, idx))

            if len(tweets) == 10:
                break

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)
