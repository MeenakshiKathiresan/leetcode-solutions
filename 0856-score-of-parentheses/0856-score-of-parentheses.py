class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = 0
        for ch in s:
            if ch == "(":
                stack.append(curr) # whatever is in this level so far, append it
                curr = 0
            else:
                if curr == 0:
                    curr += 1 # if closed immediately, just add one
                else:
                    curr *= 2 # if current already has something, double it
                curr += stack.pop() # get total of this level
        return curr