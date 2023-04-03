class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        tracker = set()
        
        for ch in s:
            if ch in tracker:
                count += 1
                tracker.clear()
            tracker.add(ch)
        if count == 0: return 1
        return count +1
            