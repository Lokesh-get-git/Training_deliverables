import time

class RateLimiter:
    def __init__(self,max_calls,seconds):
        self.max_calls=max_calls
        self.seconds=seconds
        self.calls=[]
    def allow(self):
        now= time.time()       
        self.calls=[
            t for t in self.calls if now-t<self.seconds
        ]

        if len(self.calls)>self.max_calls:
            raise RuntimeError("ratelimit exceeded")
        self.calls.append(now)