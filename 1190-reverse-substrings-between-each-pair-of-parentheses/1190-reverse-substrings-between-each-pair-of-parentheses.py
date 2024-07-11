class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(st):
            return st[::-1]
        
        brackets = []
        stack = []
        
        left = 0
        right = len(s) - 1
        
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                brackets.append((stack.pop(), i)) 
                
        for bracket in brackets:
            start, end = bracket
            start += 1
            end += 1
            
            s = s[:start] + reverse(s[start:end]) + s[end:]
            
        # remove all brackets
        s = s.replace("(", "")
        s = s.replace(")", "")
            
        return s