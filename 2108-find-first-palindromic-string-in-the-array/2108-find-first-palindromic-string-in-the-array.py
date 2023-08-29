class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            half = len(word)//2
            first = word[:half]
            
            if len(word) % 2 == 0:
                second = (word[half:])
            else:
                second = (word[half+1:])
            if first == second[::-1]:
                return word
        return ""