class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        def justify(line, space, count):
            if count == 1: 
                return line + " " * space
            else:
                space_block = space//(count-1)
                first_spaces = space % (count - 1)
            
            line_words = line.split()
            
            final = ""
            for i, line_word in enumerate(line_words):
                
                space = space_block
                
                if i < first_spaces:
                    space = space_block + 1
                
                if i == len(line_words)-1:
                    space = 0
                    
                final += line_word + (" " * space)
            
            return final
            
            
        
        
        current = ""
        res = []
        i = 0
        
        word_count = 0
        last = 0
        
        while i < len(words):
            word = words[i]
            
            if len(current) < maxWidth and len(current)+len(word) <= maxWidth:
                current += word + " "
                
                i += 1
            else:
                
                current = current[:-1]
                word_count = (abs(last - i))
                space_to_fill = (maxWidth - len(current)-1 + word_count)
                
                current = justify(current, space_to_fill, word_count)
                
                res.append(current)
                current = ""
                last = i
        
        current = current[:-1]
        current += (maxWidth - len(current)) * " "
        res.append(current)  
        
        
        return res
         
        

