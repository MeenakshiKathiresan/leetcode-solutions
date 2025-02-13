class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_count = Counter(t)
        s_count = {}

        req = len(t_count)
        req_met = 0
        left = 0

        min_len = float('inf')

        res = [0,0]

        for right, ch in enumerate(s):
            if s[right] in t_count:
                s_count[s[right]] = 1 + s_count.get(s[right], 0)

                if s[right] in t_count and s_count[s[right]] == t_count[s[right]]:
                    req_met += 1

                    # try shrinking
                    while req_met == req:
                        if (right - left + 1) < min_len:
                            min_len = right - left + 1
                            print(left, right)
                            res = [left, right]

                        if s[left] in s_count:
                            s_count[s[left]] -= 1
                            if s_count[s[left]] < t_count[s[left]]:
                                req_met -= 1

                        
                        left += 1
        return s[res[0]:res[1] + 1] if min_len != float('inf') else ""