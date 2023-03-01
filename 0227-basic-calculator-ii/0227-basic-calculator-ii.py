class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_stack = []
        n_stack = []
        
        i = 0
        ans = 0
        
        num = ''
        
        s+='+'
        
        while i < len(s):
            # digit
            if s[i] in "0123456789":
                num += s[i]
                
            elif s[i] in "/+-*" :
                n_stack.append(num)
                num = ''
                
                if len(s_stack)>0:
                    prev_symbol = s_stack.pop()
                    
                    if prev_symbol in "/*":
                        
                        a = float(n_stack.pop())
                        b = float(n_stack.pop())
                        
                        if prev_symbol == "/":
                            ans = int(b/a)
                        else:
                            ans = int(a * b)
                        
                        n_stack.append(str(ans))
                        
                
                if s[i] in "+-":
                    num += s[i]
                else:
                    s_stack.append(s[i])
                
            i+=1
        
       
        
        ans = 0
        for n in n_stack:
            ans += int(n)
            
        
        return ans