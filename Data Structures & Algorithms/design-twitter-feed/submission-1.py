from heapq import heapify,heappop
class Twitter:

    def __init__(self):
        self.user_follow: Dict[int, Set[int]] = {}
        self.user_tweet: Dict[int, List[tuple[int, int]]] = {}
        self.top_ten: List[tuple[int, int]] =[]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweet.setdefault(userId, []).append((self.time, tweetId)) 

        

    def getNewsFeed(self, userId: int) -> List[int]:
        follow =[]
        if userId in self.user_follow:
            follow.extend(self.user_follow[userId])
        follow.append(userId)

        for user in follow:
            if user in self.user_tweet:
                for timestamp, tweet in self.user_tweet[user]:
                    self.top_ten.append((-timestamp, tweet))
        
        heapify(self.top_ten)
        result = []

        k = 0
        while k < 10 and self.top_ten:
            result.append(heappop(self.top_ten)[1]) 
            k += 1
        self.top_ten= []
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follow.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follow.get(followerId, set()).discard(followeeId)
        
