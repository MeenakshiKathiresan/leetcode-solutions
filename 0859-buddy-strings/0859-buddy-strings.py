class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if s == goal:
            if len(set(s)) != len(s):
                return True
            else:
                return False
            
        if len(s) != len(goal): return False
            
        mismatch = ()
        match = False
        for i, ch in enumerate(s):
            if ch != goal[i]:
                if len(mismatch) == 0:
                    mismatch = (ch,goal[i])
                else:
                    if mismatch[0] == goal[i] and mismatch[1] == ch and not match:
                        match = True
                    else:
                        return False
        return match