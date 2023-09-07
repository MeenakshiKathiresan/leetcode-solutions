class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # 2 power grouped units
        # find groups
        
        group_count = 0
        
        ranges.sort(key=lambda x:x[0])
        group_end = 0
        
        for i, r in enumerate(ranges):
            if i == 0:
                continue
         
            if ranges[i][0] > ranges[i-1][1] and ranges[i][0] > group_end:
                group_count += 1
                
            else:
                group_end = max(group_end, ranges[i-1][1])
                
                
        modulo_value = 10**9 + 7
        return pow(2, group_count+1) % modulo_value
            
        
        
        
        