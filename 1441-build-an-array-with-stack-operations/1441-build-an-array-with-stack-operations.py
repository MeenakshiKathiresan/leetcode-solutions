class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        
        t_index = 0
        n_index = 1
        
        while t_index < len(target):
            
            if n_index == target[t_index]:
                t_index += 1
                n_index += 1
                res.append("Push")
            else:
                n_index += 1
                res.append("Push")
                res.append("Pop")
                
                
            
        return res