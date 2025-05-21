from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# নিচে কিছু sample call দেওয়া হলো
if __name__ == "__main__":
    obj = RecentCounter()
    print(obj.ping(1))     # Output: 1
    print(obj.ping(100))   # Output: 2
    print(obj.ping(3001))  # Output: 3
    print(obj.ping(3002))  # Output: 3
    print(obj.ping(7000))  # Output: 1
