class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        n = len(nums[0])
        
        def find_possibility(curr):
            if len(curr) == n and curr not in num_set:
                return curr
            if len(curr) < n:
                l = find_possibility(curr+"0")
                r = find_possibility(curr+"1")
                
                if l: return l
                if r: return r
            
       
           
            
        return find_possibility("")
                
        
        
            