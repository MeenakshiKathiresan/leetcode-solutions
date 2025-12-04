class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        i = 0
        j = n - 1

        while i < n and directions[i] == 'L':
            i += 1
        
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        res = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                res += 1
        return res
