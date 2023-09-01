class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def convertToBinary(num):
            if num == 0: return '0'
            res = ''
            while num >0:
                res += str(num%2)
                num = num//2
            return res
        
        ans = []
        for i in range(n+1):
            res = convertToBinary(i)
            ans.append(res.count('1'))
            
        return ans