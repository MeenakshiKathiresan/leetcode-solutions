class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        
        words = text.split()
        
        if len(words) == 1:
            return words[0] + (" " * (len(text)-len(words[0])))
        
        count = 0
        for word in words:
            count += len(word)
            
        spaces = len(text) - count
        per_word_space = spaces//(len(words)-1)
        
        return_word = ""
        
        for word in words:
            return_word+= word + (" "* per_word_space)
        
        return_word = return_word[:-per_word_space]
        return_word+= " "*(spaces - (per_word_space * (len(words)-1)))
        
        return return_word