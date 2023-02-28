class RecentCounter:

    def __init__(self):
        self.counter = 0    
        self.calls = []
        
    def ping(self, t: int) -> int:
        self.calls.append(t)
        
        match = []
        
        for i in range(len(self.calls)-1, -1, -1):
            if self.calls[i] <= t and self.calls[i] >= t-3000:
                match.append(self.calls[i])
            else:
                break
        
        return len(match)
        