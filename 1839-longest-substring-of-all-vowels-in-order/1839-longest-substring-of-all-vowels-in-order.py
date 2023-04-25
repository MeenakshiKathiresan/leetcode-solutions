class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        vowels = ['a','e','i','o','u']
        current = 0
        
        length = 0
        
        max_length = 0
        
        prev = -1
        
        for i, ch in enumerate(word):
            
            if  ord(ch) < prev or ord(ch) > ord(vowels[current]):
                
                current = 0
                length = 0
                
            
            
            if ord(ch) <= ord(vowels[current]) or (ch == vowels[current - 1] and word[i-1] == ch):
                length += 1
                if ch == vowels[current]:
                    current += 1
                    


                    if current == len(vowels):
                        max_length = max(max_length, length)
                        current = min(current, 4)
                        

                
            
            prev = ord(ch)
        
        return max_length