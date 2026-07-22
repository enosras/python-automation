import time
from collections import deque


class SlidingWindowLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow_request(self) -> bool:
        current_time = time.time()

        # Step 1: Remove timestamps outside of our rolling window
        while self.requests and self.requests[0] <= current_time - self.window_seconds:
            self.requests.popleft()

        # Step 2: Check if window has room
        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True

        return False


# Quick test setup: 2 requests per 3 seconds
limiter = SlidingWindowLimiter(max_requests=2, window_seconds=3)

for i in range(1, 5):
    if limiter.allow_request():
        print(f"[{i}] Request processed.")
    else:
        print(f"[{i}] Rate limit exceeded. Dropped.")
    time.sleep(0.5)
