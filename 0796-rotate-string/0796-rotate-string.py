class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        
        def isSame(i):
            reassembled = goal[i:] + goal[:i] 
            return reassembled == s
        
        
        for i, ch in enumerate(goal):
            if ch == s[0]:
                if isSame(i):
                    return True
        return False