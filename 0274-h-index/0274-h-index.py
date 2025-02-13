class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # reverse sort
        # keep adding until sum value is less than or equal to the curr

        citations.sort(reverse=True)

        sum = 0
        for c in citations:
            if sum + 1 <= c:
                sum += 1
        return sum
