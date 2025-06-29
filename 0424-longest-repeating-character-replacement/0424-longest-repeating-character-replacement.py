class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        res = 0

        for letter in char_set:
            start = 0
            swappable = k

            for end in range(len(s)):
                if s[end] != letter:
                    swappable -= 1

                # If we used more than k replacements, shrink window
                while swappable < 0:
                    if s[start] != letter:
                        swappable += 1
                    start += 1

                res = max(res, end - start + 1)

        return res
