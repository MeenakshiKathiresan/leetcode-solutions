class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. Repeat upto 26 times - maybe a set with all ch in s
        2. Sliding window - start at 0 and end also at 0
        3. move end until i can accomodate, once I can not, move start forward until 
        non matching char is removed
        4. res => get max

        "AABABB"
        """
        char_set = set(s)
        res = 0

        for letter in char_set:
            start = 0
            swappable = k
            for end in range(len(s)):
                if s[end] != letter:
                    swappable -= 1
                    
                while swappable < 0:
                    if s[start] != letter:
                        swappable += 1
                    start += 1
                res = max(res, end + 1 - start)
        return res
                