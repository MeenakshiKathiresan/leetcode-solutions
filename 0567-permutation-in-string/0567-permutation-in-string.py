class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_map = Counter(s1)
        s2_map = Counter(s2[:s1_len])

        def dict_compare():
            for k, v in s1_map.items():
                if k not in s2_map or s2_map[k] != v:
                    return False
            return True
        
        if dict_compare():
            return True

        for i in range(s1_len, s2_len, 1):
            if s2[i] not in s2_map:
                s2_map[s2[i]] = 0
            s2_map[s2[i]] += 1
            s2_map[s2[i-s1_len]] -= 1

            if s2[i] in s1_map and s2_map[s2[i]] == s1_map[s2[i]]:
                if dict_compare():
                    return True

        return False
        
        
                