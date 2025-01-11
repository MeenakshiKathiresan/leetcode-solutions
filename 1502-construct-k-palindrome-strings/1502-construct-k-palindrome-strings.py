class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)

        odd_count = 0
        for v in c.values():
            if v % 2 != 0:
                odd_count += 1
        return odd_count <= k and len(s) >= k