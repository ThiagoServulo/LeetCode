class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return len([x for x in self.requests if ((t - 3000) <= x <= t)])
        """
        count = 0
        for x in self.requests:
            if((t - 3000) <= x <= t):
                count += 1
        return count
        """

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))