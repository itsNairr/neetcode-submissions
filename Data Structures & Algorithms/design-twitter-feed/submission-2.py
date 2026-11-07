class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.posts.get(userId, 0):
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if not self.follows.get(userId, 0):
            self.follows[userId] = {userId}
        for f in self.follows[userId]:
            feed += self.posts.get(f, [])

        heapq.heapify_max(feed)
        res = []

        while len(feed) > 0 and len(res) < 10:
            res.append(heapq.heappop_max(feed)[1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId, 0):
            self.follows[followerId] = {followerId}
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
