class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverseWord(word):
            return word[::-1]
        
        res = ""
        
        for word in s.split(" "):
            res += reverseWord(word) + " "
            
        return res[:-1]