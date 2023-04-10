from collections import Counter 
class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sort by frequency
        # first 9 will have 1 per occurence
        # next will have 2 per occurence
        # next will have 3 => when choosing, first one will have only 2
        
        freq = Counter(s)
        total = 0
        
        press = 0 
        
        
        for i, count in enumerate(sorted(freq.values(), reverse=True)):
         
            if i % 9 == 0: press += 1
            total += count * press
        
        return total
        