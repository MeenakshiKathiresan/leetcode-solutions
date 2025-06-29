class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_map = Counter(s1)
        s2_map = Counter(s2[:s1_len])
        
        if s1_map == s2_map:
            return True

        for i in range(s1_len, s2_len, 1):
            if s2[i] not in s2_map:
                s2_map[s2[i]] = 0
            s2_map[s2[i]] += 1
            s2_map[s2[i-s1_len]] -= 1

            if s2[i] in s1_map and s2_map[s2[i]] == s1_map[s2[i]]:
                if s1_map == s2_map:
                    return True

        return False
        
        
                